# Changelog

Session log, newest first. One entry per session. Dates as YYYY-MM-DD.

## 2026-10-17: Speed benchmark, thinking level "low", rate limits
- What changed:
  - New `bench.py`: runs `sort_dump()` 5 times on a fixed 8-item dump. Prints each run's time, item count and wifi check, then the median, fastest and slowest. Usage: `python bench.py [low|medium]`.
  - `sorter.py`: `sort_dump(dump, thinking_level="low")`, sent as `generation_config={"thinking_level": ...}`.
  - Git: `72ec626` (pushed by Ayush) only adds a final newline to `sorter.py`, under the same message as `0fe9ae1`.
  - KB: `STATUS.md`, `CHANGELOG.md`, `DECISIONS.md` (D11, D17, new D18–D20), `NUMBERS.md`, `GOTCHAS.md` (#1, #2, #4, new #9–#11), `ARCHITECTURE.md`, `SETUP.md`, `INDEX.md`. Line numbers now refer to the commit that added `bench.py`.
  - Committed `sorter.py`, `bench.py` and the KB together. Ayush pushes.
- Why:
  - D17: measure speed properly (several runs, median) before any fix.
  - Result: low median 8.1 s vs medium 14.9 s, same results on this test, so the default is now `"low"` (D18).
- Found:
  - After about 20 calls: `429 Too Many Requests`. The SDK retries silently, so `bench.py` looked frozen for about 10 minutes (`GOTCHAS.md` #9).
  - A second API key hit the same quota. Limits are per project, not per key (`GOTCHAS.md` #10). Rule: no extra keys or projects (D19).
  - Daily free-tier limits reset at midnight Pacific (12:30 PM IST until 2026-11-01). (stated by Ayush)
- What's left: a time limit and fewer retries, then step 4 (D20). Then `requirements.txt` and step 5. Two local commits wait for Ayush to push.

## 2026-10-17: Bucket fix, more timings, KB update
- Ayush fixed the bucket name: `cant_fix_now` everywhere (commit `0fe9ae1`, "Use one name for the cant_fix_now bucket").
  - The same commit added "the college wifi is down tonight" to the sample dump (now 8 items).
  - Tested: that item landed in `cant_fix_now`. All 8 items came back, none invented. (stated by Ayush)
- Ayush pushed `ad38323` (KB) and `0fe9ae1`. GitHub `main` = `0fe9ae1` (checked with the GitHub API).
- New `sorter.py` timings, one run each: 15.3 s and 43.8 s on Ayush's own network. The earlier 49.4 s was on the hostel Wi-Fi. Cause of the variation unknown. (`NUMBERS.md`)
- Found: on the hostel Wi-Fi, DNS failed for `github.com` and the Gemini API (`GOTCHAS.md` #8).
- Next up changed: measure speed properly first (D17, replaces D16).
- KB updated: `STATUS.md`, `NUMBERS.md`, `GOTCHAS.md` (#2, #4, new #8), `DECISIONS.md` (D3, D11, D14, D16, new D17), `ARCHITECTURE.md`, `OVERVIEW.md`, `SETUP.md`, `INDEX.md`. Line numbers now refer to `0fe9ae1`.
- KB commit made by Claude Code. Ayush pushes it.

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
