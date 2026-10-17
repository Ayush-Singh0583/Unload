# Unload knowledge base: index

Start here if you are new to this repo. Read the files in this order.

| # | File | What it holds | When to read |
|---|------|---------------|--------------|
| 1 | `STATUS.md` | Where the project stands: done, in progress, next, blocked, open questions | Every session (`CLAUDE.md` loads it) |
| 2 | `OVERVIEW.md` | What Unload is, the problem, who it's for, tech stack, plan | First session |
| 3 | `ARCHITECTURE.md` | Files, classes, functions, data flow, where to change things | Before changing structure |
| 4 | `SETUP.md` | Commands to install and run; env var names | Before running or installing anything |
| 5 | `GOTCHAS.md` | Traps and known bugs | Before touching fragile parts |
| 6 | `DECISIONS.md` | Every decision: date, why, what else was considered | Before changing a decision |
| 7 | `NUMBERS.md` | Every measured number, with method, date and tag | Before quoting any number |
| 8 | `CHANGELOG.md` | Session log, newest first | To see what changed recently |

## Markers used in the KB
- **(stated by Ayush)**: Ayush said it on the date given. It is not in the code or git history.
- **(suggested by Claude, accepted by Ayush)**: Claude proposed it and Ayush agreed, on the date given.
- **VERIFIED / UNVERIFIED / CONFLICT**: tags on numbers. Defined at the top of `NUMBERS.md`.
- Facts with no marker come from the repo files, `.venv` package list, git history or the GitHub API.
- Line numbers refer to the commit that added `bench.py` (2026-10-17) unless a file says otherwise.

## Entry files in the repo root
- `CLAUDE.md`: summary and rules. Claude Code loads it automatically, and it pulls in `STATUS.md`.
- `AGENTS.md`: one line telling other assistants to read `CLAUDE.md` and `STATUS.md` first.

## Keeping the KB current
At the end of every session:
1. Update `STATUS.md`, including its "Last updated" date.
2. Add a `CHANGELOG.md` entry at the top.
3. Add new decisions to `DECISIONS.md`, new measurements to `NUMBERS.md`, new traps to `GOTCHAS.md`.
4. If the code structure changed, update `ARCHITECTURE.md` and `SETUP.md` (and their line numbers).
5. Move answered questions out of "Open questions" in `STATUS.md` and into the right file.

## Writing rules for the KB
- Only write what the files confirm, or what Ayush stated (mark it). Anything else is an open question.
- Never copy secrets. Env var names only.
- Short, plain sentences. Bullets over paragraphs. Each file under about 150 lines.
- Point to files and lines instead of copying code.
- Dates as YYYY-MM-DD.
