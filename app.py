# app.py — the FACE of your Sidekick: a Gradio chat UI.
# Run:  python app.py    then open link it Prints
 
import traceback
import gradio as gr
from agent import run_agent
 
 
def chat(message, history):
    # Gradio fills in `message` (newest) and `history` (all past turns).
    # run_agent cleans the history into the format Groq accepts.
    try:
        return run_agent(message, history)
    except Exception as e:
        traceback.print_exc()                 # full details stay in the terminal
        if type(e).__name__ == "RateLimitError":
            return "⚠️ Groq's free-plan limit was hit. Wait a minute, then try again."
        return f"⚠️ Something went wrong ({type(e).__name__}): {str(e)[:300]}"
 
 
demo = gr.ChatInterface(
    fn=chat,
    title="🔎 Research Sidekick — reads the web, keeps your notes",
    description=(
        "Share links and I'll read them, save the important bits, and recall "
        "them later — even after a restart. I remember our chat, too. "
        "Try researching a topic across a couple of pages."
    ),
    examples=[
        "Read https://en.wikipedia.org/wiki/Large_language_model and save the 3 key ideas",
        "What findings have you saved so far?",
        "Read https://anthropic.com and https://openai.com and save one difference between them",
    ],
)
 
if __name__ == "__main__":
    demo.launch()   # local only. Use demo.launch(share=True) for a public link.

