# Gotchas

Traps and known problems, most important first. Line numbers are for commit `deeb458`.

## 1. Free-tier privacy: no real personal brain dumps (stated by Ayush)
- Unload uses the Gemini free tier.
- Google's terms say human reviewers may read inputs, and say not to send personal information.
- Rule: test only with work-type tasks. Never send a real, personal brain dump.
- This applies to every test dump, every example, and every test of the future web page.
- Cleared on 2026-10-17 (stated by Ayush):
  - The sample dump in `sorter.py:49–50` is fine to send.
  - Ayush's first name in `hello.py:8` is fine to send.
- Later option: a local model on Ayush's own GPU, so no data goes to Google.

## 2. Gemini calls are very slow
- `sorter.py`: one sort took 49.4 s on 2026-10-17 (VERIFIED, 1 run).
- `hello.py`: about a minute for a five-word reply on 2026-10-17 (UNVERIFIED, a rough feel, not timed).
- Target: one sort under 10 s, measured with the timer in `sorter.py`. (stated by Ayush) Not met.
- Cause unknown. Not investigated yet.
- Must hit the target before the web page (step 5). (stated by Ayush)
- The timer in `sorter.py` wraps only `sort_dump()`. So the 49.4 s is the API call plus the Pydantic check, not imports or start-up.
- Details: `NUMBERS.md`.

## 3. Pydantic: every field needs a type annotation
- Error seen on 2026-10-17: `Field 'next_step' requires a type annotation`. (stated by Ayush)
- Cause: `next_step = Field(...)` was missing `: str`.
- Fix: `next_step: str = Field(...)`. The fix is in `sorter.py:20` now.
- Rule: inside a `BaseModel`, always write `name: type = Field(...)`, never `name = Field(...)`.

## 4. Bucket names don't match in `sorter.py`
- Decided name: `cant_fix_now`, everywhere. (stated by Ayush, 2026-10-17; `DECISIONS.md` D14)
- Code today:
  - Schema, `sorter.py:13`: `Literal["tonight", "this_week", "later", "can't fix now"]`. Wrong: must become `cant_fix_now`.
  - Prompt `RULES`, `sorter.py:30`: `cant_fix_now`. Right.
  - Print loop, `sorter.py:56`: `"cant_fix_now"`. Right.
- Effect until fixed, from reading the code (not tested):
  - If Gemini follows the schema, those items get `"can't fix now"`. The print loop looks for `"cant_fix_now"`, so they never print.
  - If Gemini follows the prompt and returns `cant_fix_now`, `model_validate_json()` raises a `ValidationError`.
- Unknown whether any sample item landed in this bucket on 2026-10-17.
- Who fixes it: Ayush, as the next step. (stated by Ayush) Guide only; don't edit the code.
- After the fix: update this entry, `ARCHITECTURE.md`, `OVERVIEW.md` and `STATUS.md`.

## 5. No `requirements.txt` yet
- Packages live only in `.venv`. A fresh clone has no list to install from.
- Adding it is Next up #2 in `STATUS.md`.
- Until then, use the install command in `SETUP.md`.

## 6. Secrets
- The key is in `.env` as `GEMINI_API_KEY`. `.env` is in `.gitignore`.
- Never print, log or commit the key. Never paste `.env` contents into a chat.
- `google-genai` also reads `GOOGLE_API_KEY`, and uses it over `GEMINI_API_KEY` if both are set. Set only one.

## 7. Small things
- `hello.py` has no `if __name__ == "__main__":` guard. Importing it makes an API call.
- `sorter.py` creates `client = genai.Client()` at import time (line 9). Anything that imports `sorter.py` (like the future FastAPI app) creates the client then.
- The model name `gemini-3.8-flash` is hard-coded in two files: `hello.py:7` and `sorter.py:38`.
- `sort_dump()` has no error handling for network or API errors.
- No automated tests. "Tested" means run by hand.
