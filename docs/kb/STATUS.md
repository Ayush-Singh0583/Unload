Last updated: 2026-10-17
Summary: Steps 1–3 done, bucket fix done, all pushed. Three single sorts took 15.3–49.4 s against a target of under 10 s. Next: measure speed properly.

## Done (working and tested)
- Step 1: `hello.py` makes one Gemini call and prints the reply. (stated by Ayush)
- Step 2: answer schema `Item` and `SortedDump` in `sorter.py`.
- Step 3: `sort_dump()` in `sorter.py` sorts the sample dump in the terminal. (stated by Ayush)
  - Tested by running `python sorter.py` by hand. No automated tests exist.
- Fixed: Pydantic error "Field 'next_step' requires a type annotation". (stated by Ayush; the fix is at `sorter.py:20`)
- Fixed: the fourth bucket is `cant_fix_now` everywhere (commit `0fe9ae1`).
  - Tested by Ayush: added "the college wifi is down tonight" to the sample dump. It landed in `cant_fix_now`. All 8 items came back, none invented. (stated by Ayush)
- Knowledge base (`docs/kb/`, `CLAUDE.md`, `AGENTS.md`) committed as `ad38323` and pushed.
- GitHub https://github.com/Ayush-Singh0583/Unload (public, branch `main`) is at `0fe9ae1` (checked 2026-10-17 with the GitHub API).

## In progress (what, which files, how far along)
- Nothing in progress.

## Next up (ordered, most important first)
Order stated by Ayush on 2026-10-17 (`DECISIONS.md` D17).
1. Measure speed properly: several runs of `python sorter.py`, take the median. Do this before trying any fix.
2. Add `requirements.txt` so a fresh clone can install the same packages.
3. Fix the speed: one sort under 10 s, measured with the timer in `sorter.py`. Cause of the slowness unknown.
4. Step 4: FastAPI `POST /sort`. Request `{"dump": "<text>"}`, response the `SortedDump` JSON (`DECISIONS.md` D15).
5. Step 5: one plain HTML page, then push to GitHub.

## Blocked / waiting on (what, and on whom)
- Step 5 (web page) waits on Next up #3 (speed under 10 s). On Ayush, with Claude as guide.
- Nothing is waiting on outside people.

## Open questions for Ayush
1. Speed measurement: how many runs per median, on which network, and the same sample dump every time?
2. Which sample dump did the 15.3 s and 43.8 s runs use: the 7-item one, or the 8-item one with the wifi line?
3. `requirements.txt`: pin exact versions (as listed in `SETUP.md`), or list package names only?
4. `POST /sort`: what should it return when Gemini fails, or when the answer doesn't fit the schema?
5. Some reasons are still "Not recorded" in `DECISIONS.md`: D2, D7, D10, D12, D14, D15, D17, and why `gemini-3.8-flash` over other Gemini models. Most "Considered" lines are also empty.
