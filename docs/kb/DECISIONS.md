# Decisions

- Every decision below was made on 2026-10-17 and is (stated by Ayush), unless a line says otherwise.
- "(suggested by Claude, accepted by Ayush)": Claude proposed it and Ayush agreed.
- "Not recorded" means Ayush has not said. Do not fill it in by guessing. Ask, then update.
- Add new decisions at the bottom with the next number. If a decision changes, add a new entry and mark the old one "Replaced by Dn".

## D1. What Unload is, and who it's for
- Date: 2026-10-17
- Decision: A brain-dump sorter. One messy message in. Items sorted into tonight / this week / later / can't fix right now, plus one small next step.
- For: students and early-career people who have too much on their mind to start anything. The first user is Ayush.
- Why: Having too much on your mind makes it hard to start anything. The `RULES` prompt in `sorter.py` says "You help a tired student clear their head."
- Considered: Not recorded.

## D2. Ayush types the code; Claude guides
- Date: 2026-10-17
- Decision: Ayush types the code. Claude explains each step and suggests the code. Claude does not take over.
- Why: Not recorded.
- Considered: Not recorded.

## D3. AI help is credited in commits
- Date: 2026-10-17
- Decision: Commits made with AI help end with the line `Co-Authored-By: Claude`. No email. No hiding that AI helped.
- Why: Ayush wants to be honest about how it was built. (suggested by Claude, accepted by Ayush) Leaving out the email is Ayush's choice.
- Considered: A trailer with an email address. Ayush chose no email.
- Seen in git: commits `deeb458`, `ad38323` and `0fe9ae1` all end with this line.

## D4. Python, google-genai, gemini-3.8-flash
- Date: 2026-10-17
- Decision: Python, the `google-genai` SDK, model `gemini-3.8-flash`, called with `client.interactions.create`.
- Why (suggested by Claude, accepted by Ayush):
  - Python: Ayush's strongest stack.
  - Gemini: free to start. Ayush used it before in a tech news chatbot. Structured output is a skill Ayush wants to show.
  - `gemini-3.8-flash` over other Gemini models: Not recorded.
- Considered: Not recorded.
- In code: `hello.py`, `sorter.py`.

## D5. Structured output with a Pydantic schema
- Date: 2026-10-17
- Decision: Gemini must answer in JSON that matches `SortedDump.model_json_schema()`. The reply is checked with `SortedDump.model_validate_json()`.
- Why: The code needs a reliable shape, and Pydantic rejects answers that don't fit it. (suggested by Claude, accepted by Ayush)
- Considered: Not recorded.

## D6. FastAPI for the API (planned)
- Date: 2026-10-17
- Decision: Use FastAPI for the API.
- Why: Python + FastAPI is Ayush's strongest stack, and Ayush's NIDS project already uses FastAPI. (suggested by Claude, accepted by Ayush)
- Considered: Not recorded.
- State: `fastapi` and `uvicorn` installed in `.venv`. No code yet.

## D7. Plain HTML page for the front end (planned)
- Date: 2026-10-17
- Decision: The front end is one plain HTML page.
- Why: Not recorded.
- Considered: Not recorded.

## D8. Free tier: no real personal brain dumps
- Date: 2026-10-17
- Decision: Never send personal information to the free-tier Gemini API. Test data must be work-type tasks.
- Scope: the rule is about real, personal brain dumps. The sample dump in `sorter.py` and Ayush's first name in `hello.py` are fine to send.
- Why: On the Gemini free tier, Google's terms say human reviewers may read inputs, and say not to send personal information.
- Considered: A local model on Ayush's own GPU. Kept as a later option.

## D9. v0 scope: one page plus /sort, no login, no database
- Date: 2026-10-17
- Decision: v0 is one page plus a `/sort` endpoint. No login. No database.
- Why: Small enough to finish in one night. Add more after Ayush has used it for a week. (suggested by Claude, accepted by Ayush)
- Considered: Microservices. Deferred: they come later, and only for splits with a clear reason (example: a separate morning-reminder service).
  - Why later: one developer and no users yet. Each split must solve a real problem. (suggested by Claude, accepted by Ayush)

## D10. Five build steps
- Date: 2026-10-17
- Decision: 1 setup + hello, 2 answer schema, 3 sorter working in the terminal, 4 FastAPI endpoint, 5 page + push to GitHub.
- Why: Not recorded.
- Considered: Not recorded.
- State: steps 1–3 done (see `STATUS.md`).

## D11. Speed must improve before the web page
- Date: 2026-10-17
- Decision: Gemini calls must get much faster before the web page (step 5).
- Target: one sort under 10 s, measured with the timer in `sorter.py`.
- Why: One sort took 49.4 s (`NUMBERS.md`). Cause unknown.
- Considered: Not recorded.
- State: not met. Single runs so far: 49.4 s, 15.3 s, 43.8 s (`NUMBERS.md`).

## D12. Public GitHub repo
- Date: 2026-10-17
- Decision: Code lives at https://github.com/Ayush-Singh0583/Unload, branch `main`, public.
- Why: Not recorded.
- Considered: Not recorded.

## D13. Keep a knowledge base in the repo
- Date: 2026-10-17
- Decision: Keep a KB in `docs/kb/`, with `CLAUDE.md` and `AGENTS.md` in the repo root as entry files.
- Why: So any AI assistant (Claude, Gemini or another) can start a new session and know the project without Ayush re-explaining.
- Considered: Not recorded.
- Rules that came with it: update `STATUS.md` and `CHANGELOG.md` every session; never quote a number unless `NUMBERS.md` marks it VERIFIED.

## D14. Fourth bucket is named `cant_fix_now`
- Date: 2026-10-17
- Decision: Use `cant_fix_now` everywhere in the code.
- Why: Not recorded.
- Considered: `"can't fix now"`, the old value in the schema at `sorter.py:13`.
- State: done in commit `0fe9ae1` and tested by Ayush. See `GOTCHAS.md` #4.

## D15. Shape of the `/sort` endpoint (suggested by Claude, accepted by Ayush)
- Date: 2026-10-17
- Decision: `POST /sort`. Request body `{"dump": "<text>"}`. Response: the `SortedDump` JSON (`items` + `next_step`).
- Why: Not recorded.
- Considered: Not recorded.
- State: not built (step 4). Error responses not decided.

## D16. Order of the next work
- Replaced by D17 (2026-10-17).
- Date: 2026-10-17
- Decision: 1 fix the bucket name, 2 add `requirements.txt`, 3 fix the speed, 4 step 4 (FastAPI `/sort`), 5 step 5 (page).
- Why: Not recorded.
- Considered: The first KB draft's order: bucket fix, speed, step 4, `requirements.txt`, step 5.

## D17. Measure speed properly before fixing it
- Date: 2026-10-17
- Decision: Before trying any speed fix, measure properly: several runs, take the median.
- New order of work: 1 measure speed, 2 add `requirements.txt`, 3 fix the speed, 4 step 4 (FastAPI `/sort`), 5 step 5 (page). The bucket fix from D16 is done.
- Why: Not stated directly. Context: three single runs gave 49.4 s, 15.3 s and 43.8 s, and the cause of the variation is unknown (`NUMBERS.md`).
- Considered: D16's order, which went straight to the speed fix.
- Replaces: D16.
