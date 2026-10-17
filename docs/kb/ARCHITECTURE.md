# Architecture

State on 2026-10-17, commit `0fe9ae1`. Two Python scripts. No package, no tests.

## Folder structure
```
Unload/
├── .env            # holds GEMINI_API_KEY. Git-ignored. Never read, print or commit it.
├── .gitignore      # ignores .venv/, .env, __pycache__/
├── .venv/          # virtual env, Python 3.14.4. Git-ignored.
├── hello.py        # step 1: one Gemini call, prints the reply
├── sorter.py       # steps 2–3: answer schema + sorter, run from the terminal
├── CLAUDE.md       # session entry file for Claude Code
├── AGENTS.md       # session entry pointer for other assistants
└── docs/kb/        # this knowledge base
```
- There is no `requirements.txt` (Next up #2), no `README.md` and no tests folder.

## Files

### `hello.py` (step 1: smoke test)
- `load_dotenv()`, then `client = genai.Client()`.
- Calls `client.interactions.create(model="gemini-3.8-flash", input="say hi to Ayush in Five Words.")`.
- Prints `interaction.output_text`.
- No `if __name__ == "__main__":` guard, so importing it makes an API call.

### `sorter.py` (steps 2–3: the sorter)

Module level:
- `load_dotenv()`, then `client = genai.Client()` (line 9). The client is made once, when the module is imported.
- `RULES` (lines 24–34): the prompt text.
  - How to split the dump: one item per distinct thing.
  - The four bucket meanings (lines 27–30).
  - "Only use things that are in the dump. Never invent new tasks."
  - Pick one `next_step`.
  - Ends with `Brain dump:` so the dump can be added right after it.

Classes (Pydantic `BaseModel`):
- `Item` (lines 11–16)
  - `text: str`: one thing from the dump, as a short clear line
  - `bucket: Literal["tonight", "this_week", "later", "cant_fix_now"]`: when to deal with it
  - `why: str`: one short reason for the bucket
- `SortedDump` (lines 18–22)
  - `items: list[Item]`
  - `next_step: str`: the single smallest action to do first, under 15 minutes
- The `Field(description=...)` texts end up in the JSON schema, so Gemini sees them.

Function:
- `sort_dump(dump: str) -> SortedDump` (lines 36–46)
  - Sends `RULES + dump` to `gemini-3.8-flash`.
  - Passes `response_format={"type": "text", "mime_type": "application/json", "schema": SortedDump.model_json_schema()}`.
  - Returns `SortedDump.model_validate_json(interaction.output_text)`.
  - Raises `pydantic.ValidationError` if the reply does not match the schema.
  - No error handling around the API call.

`__main__` block (lines 48–64):
- Uses a hard-coded sample dump of 8 items (lines 49–51).
- Times `sort_dump()` with `time.perf_counter()` (lines 53–55).
- Prints items grouped by bucket, in the order `tonight`, `this_week`, `later`, `cant_fix_now` (line 57), each with its `why`.
- Prints `Next step: ...` and `Took X.X s`.

## Data flow
```
user text  (dump: str, hard-coded in __main__ for now)
  → prompt: RULES + dump
  → client.interactions.create(model="gemini-3.8-flash",
        response_format = JSON schema from SortedDump.model_json_schema())
  → Gemini returns JSON text in interaction.output_text
  → SortedDump.model_validate_json(...)   Pydantic check; raises on mismatch
  → SortedDump object (items + next_step)
  → __main__ prints it grouped by bucket, then next_step and time taken
```

## Planned, not built
- Step 4: a FastAPI app with `POST /sort`. (suggested by Claude, accepted by Ayush; `DECISIONS.md` D15)
  - Request body: `{"dump": "<text>"}`
  - Response: the `SortedDump` JSON: `items` (each with `text`, `bucket`, `why`) and `next_step`.
  - Error responses are not decided. See `STATUS.md` open questions.
- Step 5: one plain HTML page, then push to GitHub. (stated by Ayush)
- No login and no database in v0. (stated by Ayush)
- Microservices only later, and only with a clear reason (example: a morning-reminder service). (stated by Ayush)

## Where to change things
- Model name: hard-coded twice, `hello.py:7` and `sorter.py:38`.
- Prompt wording: `RULES` in `sorter.py` (lines 24–34).
- Field meanings shown to Gemini: the `Field(description=...)` texts in `Item` and `SortedDump`.
- Bucket names: three places that must match. All say `cant_fix_now` since commit `0fe9ae1` (`DECISIONS.md` D14).
  - Schema: `sorter.py:13`
  - Prompt: `sorter.py:27–30`
  - Print loop: `sorter.py:57`
  - See `GOTCHAS.md` #4.
- Sample dump for terminal runs: `sorter.py:49–51`. Work-type tasks only (`GOTCHAS.md` #1).
