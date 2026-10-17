# Changelog

Session log, newest first. One entry per session. Dates as YYYY-MM-DD.

## 2026-10-17: Knowledge base created
- Claude Code built the KB at Ayush's request.
- Added `docs/kb/`: `INDEX.md`, `OVERVIEW.md`, `ARCHITECTURE.md`, `SETUP.md`, `STATUS.md`, `DECISIONS.md`, `NUMBERS.md`, `GOTCHAS.md`, `CHANGELOG.md`.
- Added `CLAUDE.md` and `AGENTS.md` in the repo root.
- No code changed.
- Recorded Ayush's context from 2026-10-17, marked "(stated by Ayush)".
- Checked with the GitHub API: the repo is public, and GitHub `main` is at `deeb458`.
- Found while reading the code:
  - The fourth bucket's name doesn't match in `sorter.py` (`GOTCHAS.md` #4).
  - No `requirements.txt` (`GOTCHAS.md` #5).
- Ayush answered the 10 open questions. Recorded:
  - Who it's for (`OVERVIEW.md`, D1).
  - Fourth bucket name `cant_fix_now` (D14). Ayush fixes `sorter.py:13` next.
  - New Next up order (D16) and `POST /sort` shape (D15).
  - Speed target: one sort under 10 s (`NUMBERS.md`, D11).
  - Privacy scope: real, personal brain dumps; sample dump and first name are fine (D8).
  - Install command (`SETUP.md`). Reasons for D3–D6 and D9.
- Committed the KB files only as "Add project knowledge base".
- Push failed: `github.com` did not resolve from this machine. Push pending, on Ayush.

## 2026-10-17: Steps 1–3 built and pushed
- Step 1: `hello.py` makes one Gemini call. (stated by Ayush)
- Step 2: answer schema `Item` and `SortedDump` in `sorter.py`.
- Step 3: `sort_dump()` sorts the sample dump in the terminal. (stated by Ayush)
- Bug fixed: "Field 'next_step' requires a type annotation". Added `: str`. (stated by Ayush)
- Timed: one sort took 49.4 s (VERIFIED). `hello.py` was also slow (UNVERIFIED). See `NUMBERS.md`.
- Commit `deeb458` "Sort a brain dump into buckets with Gemini structured output", 2026-10-17 02:27 +0530. It ends with `Co-Authored-By: Claude`.
- Pushed to `origin/main` at https://github.com/Ayush-Singh0583/Unload.
