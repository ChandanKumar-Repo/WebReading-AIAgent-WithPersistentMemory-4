# 🚀 Class Project — Build Your Own AI Sidekick

*AI Engineering · after Class 1 & Class 2*

---

## The mission

In two classes you went from your very first API call to a tool-using agent
with memory. Now you'll put it all together into **one real app that you would
actually use** — and share a live link to it with your friends.

You will build an **AI Sidekick**: a chat assistant, powered by a **free**
Groq model, that

1. **remembers** the conversation (like `memory_chat.py` from Class 2), and
2. can **use a tool** to do something a plain chatbot can't — the starter tool
   is **"read any web page"** (your Class 1 scraper, handed to the agent like
   `get_price` in Class 2's `agent.py`), and
3. lives inside a **Gradio chat UI** with a public share link (Class 1 & 2).

Then you make it *yours* by pointing it at a problem you genuinely care about.

> 💡 This is literally the "homework hint" from Class 2's `app.py`:
> *"pass `history` into your agent to give it memory!"* — plus one real tool.

---

## Why this matters (the "real value" part)

A chatbot that can *read the live web on demand* and *remember what you told
it* is the skeleton of most useful AI products: research assistants, study
buddies, shopping helpers, job-hunt copilots. You're not building a toy — you're
building the smallest version of a real thing, and you can keep growing it after
the course.

---

## What you must build (the core — everyone does this)

Your app **must** tick every box below. Each box maps to something you already
saw in class.

- [ ] **Uses a free Groq model** via the OpenAI client pointed at Groq's
      `base_url` — exactly like `class-1/groq_call.py`. *(No paid keys.)*
- [ ] **Has at least one tool** the model can call on its own, described with a
      tool schema — like `tools` in `class-2/agent.py`. The default tool is
      `read_webpage(url)` built from your Class 1 scraper.
- [ ] **Has memory** — past turns are fed back in so it stays consistent — like
      `class-2/memory_chat.py`.
- [ ] **Has a Gradio chat UI** with `.launch(share=True)` — like
      `class-2/app.py`.
- [ ] **Solves a real, specific job.** Not "a general chatbot." Pick a lane
      (see the menu below) and tune the system prompt + welcome message for it.

That's the whole requirement. Everything else is flavor and stretch.

---

## Pick your flavor (choose ONE, or invent your own)

Same skeleton, different personality + system prompt. Pick what excites you:

| Flavor | What it does | The tool earns its keep by… |
|--------|--------------|------------------------------|
| 📰 **Article Explainer** | Paste a news/blog URL, then ask "explain like I'm 12", "what's the bias?", "quiz me" | reading the article so answers are grounded in it |
| 🎓 **Study Buddy** | Paste a Wikipedia/docs URL, then "summarize", "make 5 flashcards", "test me" | pulling the source so it doesn't hallucinate facts |
| 💼 **Job-Hunt Copilot** | Paste a job-posting URL, then "am I a fit?", "draft a cover letter", "what should I learn?" | reading the actual JD |
| 🛍️ **Smart Shopper** | Paste a product page, then "pros/cons?", "who is this for?", "cheaper alternative?" | reading the product details |
| 🧳 **Trip Planner** | Paste a "things to do in X" page, then "3-day plan on a budget?" | reading the live destination guide |

> Want something else entirely? Great — just keep the four core boxes ticked.

---

## The rules (read these!)

- **Free tier only.** Groq's free API key is the only credential you need. No
  OpenAI billing, no paid services. Get a key at
  <https://console.groq.com/keys>.
- **Vibe-code it.** Use AI (ChatGPT, Claude, Cursor, whatever) to help you
  write, debug, and improve the code. That's encouraged — the skill is
  *directing* the AI and *understanding* the result, not typing from memory.
- **You must understand your own code.** If you can't explain a line in your
  demo, that's a red flag. Ask your AI to explain anything you pasted.
- **Never commit your `.env`.** Your key is a secret. A `.gitignore` is provided.
- **Only Class 1 & 2 tools.** `requests`, `beautifulsoup4`, `openai`,
  `python-dotenv`, `gradio`, and optionally `langchain`. No vector databases,
  no embeddings, no new frameworks. (Save those for later classes 😉)

---

## What you get to start

In the `starter/` folder:

- `tools.py` — the Class 1 scraper, ready to go. **TODO:** wrap it as a tool.
- `agent.py` — a skeleton agent loop. **TODO:** fill in the think→tool→answer
  steps and accept `history`.
- `app.py` — a near-complete Gradio chat app. **TODO:** pass `history` to your
  agent.
- `requirements.txt` and `.env.example`.

The `TODO`s are your map. Follow them in order.

---

## What shows that you made a successful solution

| Area | What's the expected behaviour |
|------|------------------------|
| **It runs** | `python app.py` launches and chats without crashing. |
| **Tool works** | The model actually calls the tool when it should (e.g. reads a URL) — we can *see* it happen. |
| **Memory works** | It remembers earlier turns (tell it your name, ask later). |
| **Real & specific** | It clearly does one useful job well; prompt + UI are tuned for it. |
| **You understand it** | You can explain the agent loop and where memory lives. |
| **Polish / stretch** | Nice UI touches, error handling, an extra tool, examples. |

---

## Stretch goals

- Add a **second tool** (e.g. a word-count/readability check, a "save note"
  tool, or a simple calculator) so the agent has a real menu to choose from.
- Add **example prompts** to the Gradio UI so first-time users know what to type.
- Handle the case where a page **fails to load** gracefully.
- Let the agent **read two pages and compare** them in one answer.
- Give it a **personality** (a themed system prompt + emoji + a fun title).

---

## What to have at the end

1. Your project folder (code) — **without** the `.env` file.
2. A short `README.md` in your folder: what it does, your chosen flavor, how to
   run it, and one thing you'd add next.

Have fun. Build something you'd actually open again. 🎉
