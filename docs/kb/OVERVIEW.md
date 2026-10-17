# Overview

## What Unload is
- A brain-dump sorter. (stated by Ayush)
- You type everything on your mind in one messy message.
- Unload splits it into separate items and puts each item in exactly one bucket.
- Bucket meanings come from the `RULES` prompt in `sorter.py`:

| Bucket (Ayush's words) | Name in code | Meaning |
|---|---|---|
| tonight | `tonight` | Small, or needed to rest tonight |
| this week | `this_week` | Has to happen in the next 7 days |
| later | `later` | Goals or plans with no deadline this week |
| can't fix right now | `cant_fix_now` (decided; the schema at `sorter.py:13` still says `"can't fix now"`) | Outside your control right now, or a feeling to acknowledge, not a task |

- Ayush decided on `cant_fix_now` everywhere (2026-10-17). Until `sorter.py:13` is fixed, the code doesn't match. See `GOTCHAS.md` #4.
- Each item also gets a one-line reason for its bucket (the `why` field).
- Unload also picks one small next step: the smallest useful action to do first. The schema asks for under 15 minutes.
- The prompt says: only use things that are in the dump, and never invent new tasks.

## The problem it solves
- People with too much on their mind can't start anything. (stated by Ayush)
- Unload turns one messy message into a short sorted list and one first step.
- The prompt in `sorter.py` puts it as: "You help a tired student clear their head."

## Who it's for (stated by Ayush)
- Students and early-career people who have too much on their mind to start anything.
- The first user is Ayush.
- The `RULES` prompt in `sorter.py` describes the user as "a tired student".

## How it is built (stated by Ayush)
- Ayush builds it and types the code.
- Claude is a guide: it explains each step and suggests the code.
- Commits made with AI help end with the line `Co-Authored-By: Claude` (no email, Ayush's choice).
- No hiding that AI helped.

## Tech stack

| Part | Choice | State on 2026-10-17 |
|---|---|---|
| Language | Python | In use. `.venv` has Python 3.14.4 |
| LLM SDK | `google-genai` | In use |
| Model | `gemini-3.8-flash`, called with `client.interactions.create` | In use |
| Output format | Structured output with a Pydantic schema | In use (`SortedDump` in `sorter.py`) |
| Secrets | `python-dotenv` loads `.env` | In use |
| API | FastAPI | Planned (stated by Ayush). Installed in `.venv`, not used in code yet |
| Front end | One plain HTML page | Planned (stated by Ayush). Not started |
| Login, database | None in v0 | By design (stated by Ayush) |

## Privacy (stated by Ayush)
- Unload uses the Gemini free tier.
- Google's terms say human reviewers may read inputs, and say not to send personal information.
- So: test only with work-type tasks.
- Later option: a local model on Ayush's own GPU.

## Plan (stated by Ayush)
- v0: one page plus a `/sort` endpoint. No login, no database.
- Microservices come later, and only for splits with a clear reason.
  - Example: a separate morning-reminder service.
- Build steps:
  1. Setup + hello
  2. Answer schema
  3. Sorter working in the terminal
  4. FastAPI endpoint: `POST /sort`, body `{"dump": "<text>"}`, returns the `SortedDump` JSON (`DECISIONS.md` D15)
  5. Page + push to GitHub
- Steps 1–3 are done. See `STATUS.md`.
- Speed target before the page: one sort under 10 s (`NUMBERS.md`).
- Reasons for the stack and scope: `DECISIONS.md` D4–D9.

## Links
- Repo: https://github.com/Ayush-Singh0583/Unload
  - Public, default branch `main`. Checked 2026-10-17 with the GitHub API.
