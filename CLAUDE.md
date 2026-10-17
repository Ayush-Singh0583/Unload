# Unload
Unload is a brain-dump sorter. You type everything on your mind in one messy message. It splits the message into items, puts each item in one bucket (tonight / this week / later / can't fix right now), and picks one small next step. It is for students and early-career people who have too much on their mind to start anything; Ayush is the first user. It is written in Python and uses the `google-genai` SDK with `gemini-3.8-flash` and structured output checked by a Pydantic schema (`sorter.py`). A FastAPI `/sort` endpoint and one plain HTML page are planned. Ayush builds it and types the code. Claude is a guide that explains each step and suggests code. Repo: https://github.com/Ayush-Singh0583/Unload (public, branch `main`).

## Read at the start of every session
@docs/kb/STATUS.md

## Read when needed
- `docs/kb/INDEX.md`: map of the knowledge base
- `docs/kb/ARCHITECTURE.md`: before changing structure
- `docs/kb/SETUP.md`: before running or installing anything
- `docs/kb/NUMBERS.md`: before quoting any number
- `docs/kb/GOTCHAS.md`: before touching fragile parts

## Rules
- Guide, don't take over: explain the idea and a small example first, then give code for Ayush to type.
- Never commit .env, and never print or log the API key.
- Never send personal information to the free-tier Gemini API. Test data must be work-type tasks.
- Every commit made with AI help ends with the line "Co-Authored-By: Claude".
- At the end of every session, update STATUS.md and add a CHANGELOG.md entry.
- Record every important decision in DECISIONS.md.
- Never quote a number unless NUMBERS.md marks it VERIFIED.
