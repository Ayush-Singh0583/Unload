# Numbers

Every measured number goes here. Do not quote a number anywhere unless this file marks it VERIFIED.

## Tags
- **VERIFIED**: measured by code in this repo (you can find the timer or counter in the file), with a date and result recorded.
- **UNVERIFIED**: an estimate, or not measured by code in the repo. Do not quote it as fact.
- **CONFLICT**: two sources disagree. The notes say which ones.

## Measurements

| What | Value | Date | How measured | Tag |
|---|---|---|---|---|
| One sort, `python sorter.py` | 49.4 s | 2026-10-17 | `time.perf_counter()` around `sort_dump(dump)` in `sorter.py` (lines 52–54), printed at line 63. Sample dump at lines 49–50. One run, reported by Ayush. | VERIFIED (1 run) |
| One call, `python hello.py` (five-word reply) | about 1 minute | 2026-10-17 | Not timed. A rough feel (confirmed by Ayush, 2026-10-17). | UNVERIFIED |

### Notes
- The 49.4 s covers only the `sort_dump()` call: the Gemini request plus the Pydantic check.
  - It does not include Python start-up, imports or creating `genai.Client()`.
- The `hello.py` figure was never timed. Keep it UNVERIFIED (stated by Ayush).
- Neither number was re-run in the 2026-10-17 knowledge-base session.
- Cause of the slowness: unknown. See `GOTCHAS.md` #2.

## Targets (goals, not measurements)

| Target | Value | Set on | How it will be measured |
|---|---|---|---|
| One sort | under 10 s | 2026-10-17 (stated by Ayush) | The `time.perf_counter()` timer in `sorter.py` (lines 52–54) |

- Latest measurement against it: 49.4 s (VERIFIED, 1 run). Not met.

## Fixed values in the code (limits, not measurements)
These are rules written into the prompt or schema. They are not measured results.

| Value | Where | Meaning |
|---|---|---|
| under 15 minutes | `sorter.py:21` (`next_step` description) | The next step must take under 15 minutes |
| 7 days | `sorter.py:28` (`RULES`) | `this_week` means it has to happen in the next 7 days |
| 4 buckets | `sorter.py:13` (`Item.bucket`) | tonight, this_week, later, and the fourth bucket (decided name `cant_fix_now`) |
| 5 words | `hello.py:8` | The hello prompt asks for five words |

## Environment (from `.venv`, 2026-10-17)
- Python 3.14.4.
- Package versions are listed in `SETUP.md`.

## How to add a number
- Add a row: what, value, date (YYYY-MM-DD), exact method (file and line of the timer), tag.
- Say how many runs it is based on.
- If a new measurement disagrees with an old one, keep both rows and tag them CONFLICT until explained.
