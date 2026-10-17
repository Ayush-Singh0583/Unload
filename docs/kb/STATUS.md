Last updated: 2026-10-17
Summary: Steps 1–3 done. Sorting now uses thinking level "low": median 8.1 s over 5 runs, but single runs still reach 40.8 s. Next: a time limit and fewer retries, then step 4.

## Done (working and tested)
- Steps 1–3: Gemini call, answer schema, sorter working in the terminal. (stated by Ayush)
- Bucket name is `cant_fix_now` everywhere (commit `0fe9ae1`), tested by Ayush.
- Speed measured properly (D17): new `bench.py` runs `sort_dump()` 5 times and prints each time, the median, fastest and slowest.
- `sort_dump()` takes `thinking_level`, default `"low"` (`sorter.py:36`; `DECISIONS.md` D18).
  - Benchmark, 5 runs each, Ayush's own network, 8-item dump: low median 8.1 s, medium median 14.9 s. Both gave 8 items and the wifi line in `cant_fix_now` in 5 of 5 runs. (stated by Ayush; `NUMBERS.md`)
- Found why runs looked frozen: on `429 Too Many Requests`, the SDK retries silently with backoff (`GOTCHAS.md` #9).

## In progress (what, which files, how far along)
- Nothing in progress. The time limit and retry change is not started.

## Next up (ordered, most important first)
Order stated by Ayush on 2026-10-17 (`DECISIONS.md` D20).
1. Add a time limit and fewer retries to the Gemini call in `sort_dump()` (`sorter.py`), so failures are fast and clear.
2. Step 4: FastAPI `POST /sort`. Request `{"dump": "<text>"}`, response the `SortedDump` JSON (D15).
3. Add `requirements.txt`. (Carried over; not placed by Ayush this time. See question 3.)
4. Step 5: one plain HTML page, then push to GitHub.

## Blocked / waiting on (what, and on whom)
- Free-tier quota was hit on 2026-10-17, on two keys of the same project. API calls may fail until it resets. Daily limits reset at midnight Pacific (`GOTCHAS.md` #10).
- Push: GitHub `main` is at `72ec626`. Local commits `0bdd25d` (KB update) and the `bench.py` commit wait for Ayush to push.
- Step 5 (web page) waits on the speed target (D11). On Ayush, with Claude as guide.

## Open questions for Ayush
1. Speed target (D11): does "under 10 s" mean the median (low: 8.1 s, met) or every run (slowest: 40.8 s, not met)?
2. Which limit did the 429 hit: per-minute or per-day? It decides whether to wait a minute or until the daily reset.
3. `requirements.txt`: where does it go in Next up (it was #2), and should it pin exact versions?
4. The 88.2 s run: was it printed by `bench.py`, or timed another way? `bench.py` prints no time for a run that ends in an error.
5. `bench.py` with no argument runs `"medium"`, but the app default is `"low"`. Change the bench default? (`GOTCHAS.md` #11)
6. `POST /sort`: what should it return when Gemini fails, times out, or the answer doesn't fit the schema?
7. Which sample dump did the 15.3 s and 43.8 s runs use: 7 items or 8?
8. Reasons still "Not recorded" in `DECISIONS.md`: D2, D7, D10, D12, D14, D15, D17, and why `gemini-3.8-flash`.
