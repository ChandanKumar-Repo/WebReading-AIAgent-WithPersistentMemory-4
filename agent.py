# agent.py — brain + loop.
#   • runs on FREE Groq (OpenAI-compatible client pointed at Groq),
#   • takes `history` so it REMEMBERS the chat,
#   • drives a whole TOOL MENU (read the web / save / recall).
 
import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from tools import TOOLS_SCHEMA, TOOL_FUNCTIONS
 
load_dotenv()
 
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found. Add it to your .env file.")
 
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)
MODEL = "openai/gpt-oss-120b"  # free Groq model that supports tools
 
SYSTEM_PROMPT = (
    "You are Research Sidekick, a sharp, friendly research assistant.\n"
    "Your workflow:\n"
    "• When the user shares a URL or asks about a page, call read_webpage and "
    "answer using ONLY what you found - never make things up.\n"
    "• When you find something clearly worth keeping (or the user asks you to "
    "remember it), call save_finding with a short topic.\n"
    "• When the user asks what you've saved, or you need past notes to answer, "
    "call list_findings.\n"
    "For multi-source jobs, read each page first, then save the key points, then "
    "summarise. Cite which source each point came from. Reply in clean markdown."
)
 
MAX_TOOL_HOPS = 8            # safety cap so the loop can't run forever
MAX_HISTORY_MESSAGES = 20    # keep only the last ~10 turns so long chats stay within free-tier limits
 
 
def _text_of(content):
    """Gradio 6 sends message content as a list of blocks, e.g.
    [{"type": "text", "text": "hi"}]. The Groq API wants a plain string."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(
            b.get("text", "")
            for b in content
            if isinstance(b, dict) and b.get("type") == "text"
        )
    return str(content)
 
 
def clean_history(history):
    """Turn Gradio's history into exactly what Groq accepts:
    [{"role": "user"|"assistant", "content": "plain text"}, ...].
    Gradio adds extra keys (metadata, options) that Groq rejects with a 400 error."""
    cleaned = []
    for m in history or []:
        if not isinstance(m, dict):
            continue
        text = _text_of(m.get("content", ""))
        if m.get("role") in ("user", "assistant") and text.strip():
            cleaned.append({"role": m["role"], "content": text})
    cleaned = cleaned[-MAX_HISTORY_MESSAGES:]
    while cleaned and cleaned[0]["role"] != "user":   # always start with a user message
        cleaned.pop(0)
    return cleaned
 
 
def _run_tool(call):
    """Run ONE tool the model asked for. Never raises: errors become text the model can read."""
    name = call.function.name
    fn = TOOL_FUNCTIONS.get(name)
    if fn is None:
        return f"Unknown tool: {name}"
    try:
        args = json.loads(call.function.arguments or "{}")
        return str(fn(**args))
    except Exception as e:
        return f"Tool error in {name}: {type(e).__name__}: {e}"
 
 
def run_agent(user_message, history=None):
    """One chat turn: think -> (use any tools it needs) -> answer.
    `history` = in-chat memory; the notes file = across-session memory."""
 
    # system prompt + CLEANED past turns + the new message
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(clean_history(history))
    messages.append({"role": "user", "content": _text_of(user_message)})
 
    # The loop: keep going while the model wants to use tools.
    for _ in range(MAX_TOOL_HOPS):
        response = client.chat.completions.create(
            model=MODEL, messages=messages, tools=TOOLS_SCHEMA)
        msg = response.choices[0].message
 
        # No tool requested → this is the final answer.
        if not msg.tool_calls:
            return msg.content or "Sorry, I couldn't come up with an answer. Please try again."
 
        # Otherwise: record the request, run each tool, feed results back.
        messages.append(msg)
        for call in msg.tool_calls:
            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": _run_tool(call),
            })
        # loop again so the model can use the results (and maybe call more tools)
 
    # Ran out of hops — ask for a final answer with no more tools.
    messages.append({"role": "user", "content":
                     "Stop using tools. Give your best final answer now using what you already found."})
    final = client.chat.completions.create(model=MODEL, messages=messages)
    return final.choices[0].message.content or "Sorry, I ran out of steps. Please try a simpler request."
 
 
if __name__ == "__main__":
    print(run_agent("Read https://anthropic.com and save one key finding about them."))
    print("---")
    print(run_agent("What have you saved so far?"))
 
