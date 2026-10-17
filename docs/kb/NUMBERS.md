# Numbers

Every measured number goes here. Do not quote a number anywhere unless this file marks it VERIFIED.

## Tags
- **VERIFIED**: measured by code in this repo (you can find the timer or counter in the file), with a date and result recorded.
- **UNVERIFIED**: an estimate, or not measured by code in the repo. Do not quote it as fact.
- **CONFLICT**: two sources disagree. The notes say which ones.

## Measurements
All results reported by Ayush. Rows are in the order the runs happened.

| What | Value | Date | Network | Sample dump | Tag |
|---|---|---|---|---|---|
| One sort, `python sorter.py` | 49.4 s | 2026-10-17 | Hostel Wi-Fi | 7 items (commit `deeb458`) | VERIFIED (1 run) |
| One sort, `python sorter.py` | 15.3 s | 2026-10-17 | Ayush's own network | Not recorded | VERIFIED (1 run) |
| One sort, `python sorter.py` | 43.8 s | 2026-10-17 | Ayush's own network | Not recorded | VERIFIED (1 run) |
| One call, `python hello.py` (five-word reply) | about 1 minute | 2026-10-17 | Not recorded | n/a | UNVERIFIED |

How the `sorter.py` rows were measured:
- `time.perf_counter()` around `sort_dump(dump)` in `sorter.py`, printed by the `Took X.X s` line.
- Lines 53–55 and 64 at commit `0fe9ae1` (lines 52–54 and 63 at `deeb458`; lines 55–57 and 66 now).
- These three runs were made before `thinking_level` existed, so no thinking level was sent.

How the `hello.py` row was measured:
- Not timed. A rough feel (confirmed by Ayush, 2026-10-17). Keep it UNVERIFIED.

### Notes
- Times vary a lot between runs, even on the same network (15.3 s and 43.8 s). Cause unknown. (stated by Ayush)
- Measuring properly (several runs, median) was done with `bench.py`. See the next section.
- The timer covers only the `sort_dump()` call: the Gemini request plus the Pydantic check.
  - It does not include Python start-up, imports or creating `genai.Client()`.
- On the hostel Wi-Fi, DNS also failed for the Gemini API that day. See `GOTCHAS.md` #8.

## Benchmark: `bench.py` (2026-10-17)
5 runs per setting, Ayush's own network, fixed 8-item dump (`bench.py:7–9`). Results reported by Ayush.

| Thinking level | Runs | Median | Fastest | Slowest | Results | Tag |
|---|---|---|---|---|---|---|
| `medium` | 5 | 14.9 s | not recorded | 45.5 s | 8 items and wifi line right, 5 of 5 | VERIFIED (5 runs) |
| `low` | 5 | 8.1 s | not recorded | 40.8 s | 8 items and wifi line right, 5 of 5 | VERIFIED (5 runs) |

- Command: `python bench.py <level>`.
- Timer: `time.perf_counter()` around `sort_dump()` (`bench.py:17–19`). Median with `statistics.median` (`bench.py:27`).
- Low's median is about 45% lower than medium's (8.1 s vs 14.9 s). Computed from the two medians above.
- Caveat: only 5 runs and one check per setting. (stated by Ayush)

## Rate-limit observations (2026-10-17, stated by Ayush)

| What | Value | How measured | Tag |
|---|---|---|---|
| Calls before the first `429 Too Many Requests` | about 20 | Not counted by code | UNVERIFIED |
| Time `bench.py` looked frozen during silent retries | about 10 minutes | Not timed by code | UNVERIFIED |
| One run before the "exceeded a quota" error (second key) | 88.2 s | Not recorded. `bench.py` prints no time for a run that ends in an error | UNVERIFIED |

- The ~30 s spikes in the timings (for example 40.8 s against a median of 8.1 s) are probably silent retries. Not confirmed yet. (stated by Ayush; `GOTCHAS.md` #9)

## Targets (goals, not measurements)

| Target | Value | Set on | How it will be measured |
|---|---|---|---|
| One sort | under 10 s | 2026-10-17 (stated by Ayush) | The `time.perf_counter()` timer in `sorter.py` |

- Single runs, no thinking level sent: 49.4 s, 15.3 s, 43.8 s (VERIFIED, 1 run each). Not met.
- `bench.py`, low: median 8.1 s (under 10 s), slowest 40.8 s (over). Whether the target means the median or every run is open (`STATUS.md`).

## Fixed values in the code (limits, not measurements)
These are rules written into the prompt or schema. They are not measured results.

| Value | Where | Meaning |
|---|---|---|
| under 15 minutes | `sorter.py:21` (`next_step` description) | The next step must take under 15 minutes |
| 7 days | `sorter.py:28` (`RULES`) | `this_week` means it has to happen in the next 7 days |
| 4 buckets | `sorter.py:13` (`Item.bucket`) | `tonight`, `this_week`, `later`, `cant_fix_now` |
| 5 words | `hello.py:8` | The hello prompt asks for five words |
| `"low"` | `sorter.py:36` | Default `thinking_level` of `sort_dump()` |
| `"medium"` | `bench.py:11` | Thinking level `bench.py` uses when run with no argument |
| 5 runs | `bench.py:12` | Runs per `bench.py` call |

## Environment (from `.venv`, 2026-10-17)
- Python 3.14.4.
- Package versions are listed in `SETUP.md`.

## How to add a number
- Add a row: what, value, date (YYYY-MM-DD), exact method (file and line of the timer), tag.
- Say how many runs it is based on. With several runs, give the median.
- For timings, also record the network and which sample dump was used (commit or item count).
- If a new measurement disagrees with an old one, keep both rows and tag them CONFLICT until explained.
