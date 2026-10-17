# Gotchas

Traps and known problems. Line numbers are for commit `0fe9ae1`.
Entry numbers stay fixed so other files can point to them. New entries go at the end.

## 1. Free-tier privacy: no real personal brain dumps (stated by Ayush)
- Unload uses the Gemini free tier.
- Google's terms say human reviewers may read inputs, and say not to send personal information.
- Rule: test only with work-type tasks. Never send a real, personal brain dump.
- This applies to every test dump, every example, and every test of the future web page.
- Cleared on 2026-10-17 (stated by Ayush):
  - The sample dump in `sorter.py:49–51` is fine to send.
  - Ayush's first name in `hello.py:8` is fine to send.
- Later option: a local model on Ayush's own GPU, so no data goes to Google.

## 2. Gemini calls are slow, and times vary a lot
- `sorter.py`, one run each on 2026-10-17: 49.4 s (hostel Wi-Fi), then 15.3 s and 43.8 s (Ayush's own network). All VERIFIED.
- `hello.py`: about a minute for a five-word reply (UNVERIFIED, a rough feel, not timed).
- Times vary a lot between runs, even on the same network. Cause unknown. (stated by Ayush)
- Target: one sort under 10 s, measured with the timer in `sorter.py`. (stated by Ayush) Not met.
- Must hit the target before the web page (step 5). (stated by Ayush)
- Measure properly first (several runs, median), before trying any fix. (stated by Ayush)
- The timer wraps only `sort_dump()`: the API call plus the Pydantic check, not imports or start-up.
- Details: `NUMBERS.md`.

## 3. Pydantic: every field needs a type annotation
- Error seen on 2026-10-17: `Field 'next_step' requires a type annotation`. (stated by Ayush)
- Cause: `next_step = Field(...)` was missing `: str`.
- Fix: `next_step: str = Field(...)`. The fix is in `sorter.py:20` now.
- Rule: inside a `BaseModel`, always write `name: type = Field(...)`, never `name = Field(...)`.

## 4. Bucket names live in three places (fixed 2026-10-17)
- The fourth bucket was `"can't fix now"` in the schema, but `cant_fix_now` in the prompt and print loop.
- Fixed by Ayush in commit `0fe9ae1`: now `cant_fix_now` everywhere (`DECISIONS.md` D14).
- Tested by Ayush: "the college wifi is down tonight" landed in `cant_fix_now`. All 8 sample items came back, none invented. (stated by Ayush)
- The trap stays: each bucket name is written in three places, and all three must match.
  - Schema: `sorter.py:13`
  - Prompt `RULES`: `sorter.py:27–30`
  - Print loop: `sorter.py:57`
- From reading the code: if they don't match, items in that bucket either never print, or `model_validate_json()` raises a `ValidationError`.

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

## 8. Hostel Wi-Fi: DNS fails for GitHub and Gemini (stated by Ayush)
- On the hostel Wi-Fi on 2026-10-17, DNS failed for `github.com` and for the Gemini API.
- Error: `Temporary failure in name resolution`.
- Fix: switch to another network.
- In the KB session the same day, `git push` from this machine failed with `Could not resolve host: github.com`, while `api.github.com` still resolved. The network in use then was not recorded.
