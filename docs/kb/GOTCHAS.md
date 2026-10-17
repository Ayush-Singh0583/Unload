# Gotchas

Traps and known problems. Line numbers are for the commit that added `bench.py` (2026-10-17).
Entry numbers stay fixed so other files can point to them. New entries go at the end.

## 1. Free-tier privacy: no real personal brain dumps (stated by Ayush)
- Unload uses the Gemini free tier.
- Google's terms say human reviewers may read inputs, and say not to send personal information.
- Rule: test only with work-type tasks. Never send a real, personal brain dump.
- This applies to every test dump, every example, and every test of the future web page.
- Cleared on 2026-10-17 (stated by Ayush):
  - The sample dump in `sorter.py:51–53` (same items in `bench.py:7–9`) is fine to send.
  - Ayush's first name in `hello.py:8` is fine to send.
- Later option: a local model on Ayush's own GPU, so no data goes to Google.

## 2. Gemini calls are slow, and times vary a lot
- Single runs before `thinking_level` existed (2026-10-17): 49.4 s (hostel Wi-Fi), then 15.3 s and 43.8 s (Ayush's own network). All VERIFIED.
- `bench.py`, 5 runs each: medium median 14.9 s (slowest 45.5 s); low median 8.1 s (slowest 40.8 s). VERIFIED.
- Fix so far: default thinking level `"low"` (D18).
- The slowest runs are still far above the median. Probably the SDK's silent retries (#9). Not confirmed yet. (stated by Ayush)
- `hello.py`: about a minute for a five-word reply (UNVERIFIED, a rough feel, not timed).
- Target: one sort under 10 s (D11). Low's median meets it; the slowest run does not.
- Must hit the target before the web page (step 5). (stated by Ayush)
- The timer wraps only `sort_dump()`: the API call plus the Pydantic check, not imports or start-up.
- Next: a time limit and fewer retries (D20). Details: `NUMBERS.md`.

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
  - Print loop: `sorter.py:59`
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

## 9. A 429 looks like a freeze: the SDK retries silently (stated by Ayush)
- On 2026-10-17, after about 20 calls, `bench.py` got `429 Too Many Requests`.
- It looked frozen for about 10 minutes.
- Cause, seen in the traceback: the SDK retries with backoff (`retry_with_attempt_count_backoff`, then `time.sleep`). That function is in `.venv/lib/python3.14/site-packages/google/genai/_gaos/utils/retries.py`.
- This probably also explains the ~30 s spikes in the timings. Not confirmed yet.
- Fix: not done yet. Next up #1: a time limit and fewer retries, so failures are fast and clear (D20).
- Until then, a run that seems frozen may be retrying a 429.

## 10. Free-tier quota is per project, not per key (stated by Ayush)
- On 2026-10-17, a second API key also hit the quota: `Your project has exceeded a quota`.
- Limits are per project. Another key in the same project does not help.
- One run took 88.2 s before the error, again from silent retries (#9). How it was timed is not recorded (`NUMBERS.md`).
- Rule: don't work around limits with more keys or projects (D19).
- Daily free-tier limits reset at midnight Pacific time: 12:30 PM IST.
  - 12:30 PM IST holds while the US is on daylight time. It ends on 2026-11-01; after that, midnight Pacific is 1:30 PM IST (checked with `date` and the tz database).

## 11. `bench.py` quirks (from reading the code)
- Ayush's description says `bench.py` checks that every run returns 8 items with the wifi line in `cant_fix_now`. The code prints the item count and a wifi check for each run (`bench.py:21–25`). It does not fail or count passes; you read the output.
- With no argument it uses `"medium"` (`bench.py:11`), not the app default `"low"` (`sorter.py:36`).
- The wifi check looks for `"wifi"` in the lowercased text. An item written as "Wi-Fi" would print `wifi correct: False` even if its bucket is right.
- The level argument is not checked. The SDK accepts `minimal`, `low`, `medium` and `high` (`google/genai/_gaos/types/interactions/thinkinglevel.py` in `.venv`).
- Each `bench.py` run makes 5 API calls against the free-tier quota (#10).
