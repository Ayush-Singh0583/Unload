Last updated: 2026-10-17
Summary: Steps 1–3 done and on GitHub. One sort took 49.4 s against a target of under 10 s. Next: Ayush fixes the bucket name in `sorter.py`.

## Done (working and tested)
- Step 1: `hello.py` makes one Gemini call and prints the reply. (stated by Ayush)
- Step 2: answer schema `Item` and `SortedDump` in `sorter.py`.
- Step 3: `sort_dump()` in `sorter.py` sorts the sample dump in the terminal. (stated by Ayush)
  - Tested by running `python sorter.py` by hand. No automated tests exist.
  - Known bug: the fourth bucket's name doesn't match, so those items may never print. See `GOTCHAS.md` #4.
- Fixed: Pydantic error "Field 'next_step' requires a type annotation". (stated by Ayush; the fix is at `sorter.py:20`)
- Pushed to https://github.com/Ayush-Singh0583/Unload, branch `main`, public. Code commit: `deeb458`.
- Knowledge base (`docs/kb/`, `CLAUDE.md`, `AGENTS.md`) committed locally as "Add project knowledge base" on 2026-10-17. Push pending (see Blocked).
- First round of open questions answered by Ayush on 2026-10-17. Answers are in `OVERVIEW.md`, `DECISIONS.md`, `NUMBERS.md`, `SETUP.md` and `GOTCHAS.md`.

## In progress (what, which files, how far along)
- Nothing in progress.

## Next up (ordered, most important first)
Order stated by Ayush on 2026-10-17 (`DECISIONS.md` D16).
1. Fix the bucket name at `sorter.py:13`: change `"can't fix now"` to `cant_fix_now`. Lines 30 and 56 already use `cant_fix_now`. Ayush makes this change; guide only, don't edit the code.
2. Add `requirements.txt` so a fresh clone can install the same packages.
3. Fix the speed: one sort under 10 s, measured with the timer in `sorter.py`. Cause of the slowness unknown.
4. Step 4: FastAPI `POST /sort`. Request `{"dump": "<text>"}`, response the `SortedDump` JSON (`DECISIONS.md` D15).
5. Step 5: one plain HTML page, then push to GitHub.

## Blocked / waiting on (what, and on whom)
- Step 5 (web page) waits on Next up #3 (speed under 10 s). On Ayush, with Claude as guide.
- Push of the KB commit to `origin/main`: on 2026-10-17, `github.com` did not resolve from this machine (`api.github.com` did). On Ayush: run `git push origin main` once DNS works. `git status -sb` shows "ahead" while it is still unpushed.
- Nothing is waiting on outside people.

## Open questions for Ayush
1. `requirements.txt`: pin exact versions (as listed in `SETUP.md`), or list package names only?
2. `POST /sort`: what should it return when Gemini fails, or when the answer doesn't fit the schema?
3. Some reasons are still "Not recorded" in `DECISIONS.md`: D2 (Ayush types, Claude guides), D7 (plain HTML page), D10 (five build steps), D12 (public repo), D14 (bucket name), D15 (`/sort` shape), D16 (work order), and why `gemini-3.8-flash` over other Gemini models. Most "Considered" lines are also empty.
