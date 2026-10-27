# Your AI Research Sidekick — Starter Kit

Everything you need to start is here. Read `../PROBLEM_STATEMENT.md` first for
the mission, milestones, and rules.

## Setup (once)

```bash
# 1. (recommended) a fresh virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 2. install the free libraries
pip install -r requirements.txt

# 3. add your FREE Groq key
cp .env.example .env              # Windows: copy .env.example .env
#    then open .env and paste your key from https://console.groq.com/keys
```

## Build it milestone by milestone

The `TODO`s in the code are numbered to match these. Do them in order — each
milestone should *work on its own* before you move to the next.

| # | Milestone | File(s) | You'll fill in |
|---|-----------|---------|----------------|
| 0 | First reply on Groq | `agent.py` | point the client at Groq |
| 1 | Reading tool | `tools.py`, `agent.py` | `read_webpage` schema + the tool loop |
| 2 | Chat memory | `agent.py`, `app.py` | pass `history` through |
| 3 | Tool menu | `tools.py` | build `save_finding` + `list_findings` + their schemas |
| 4 | Memory that survives restart | (test) | save → quit → relaunch → still there |
| 5 | Multi-step job | `agent.py` | the loop chains 2+ tools in one turn |
| 6 | Make it yours | `agent.py`, `app.py` | system prompt + title/examples for your flavor |

## Test as you go

```bash
python tools.py    # do the 3 tools work? (check notes.json appears)
python agent.py    # does it chat, read a URL, and save/recall?
python app.py      # does the chat app launch with a share link?
```

## Stuck?

- Model won't call a tool → make the tool `description` say *when* to use it, and
  confirm you pass `tools=TOOLS_SCHEMA` in the request.
- It forgets mid-chat → you haven't passed `history` into the agent yet (TODO 2).
- Findings vanish on restart → make sure `save_finding` actually writes
  `notes.json` (not just an in-memory list).