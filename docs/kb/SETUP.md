# Setup

Known working environment on 2026-10-17: Linux, Python 3.14.4 (`/usr/bin/python3`).
Run every command from the repo root.

## 1. Get the code
```bash
git clone https://github.com/Ayush-Singh0583/Unload.git
cd Unload
```

## 2. Create and activate the virtual env
```bash
python3 -m venv .venv
source .venv/bin/activate
```
- `.venv/pyvenv.cfg` shows the current env was made with `/usr/bin/python3 -m venv .venv`.

## 3. Install packages
There is no `requirements.txt` yet (it is Next up #2 in `STATUS.md`). This is the command Ayush used (stated by Ayush):
```bash
pip install -U google-genai fastapi "uvicorn[standard]" python-dotenv
```
- `pydantic` is not in the command. It comes in as a dependency of both `google-genai` and `fastapi` (`pip show` lists it under "Requires").
- `"uvicorn[standard]"` adds uvicorn's extras. `.venv` has `httptools`, `uvloop`, `watchfiles` and `websockets`.
- `fastapi` and `uvicorn` are for step 4. No code uses them yet.
- Once `requirements.txt` exists, use `pip install -r requirements.txt` instead.

Versions in `.venv` on 2026-10-17 (from `pip list`):

| Package | Version | Used by |
|---|---|---|
| google-genai | 2.31.0 | `hello.py`, `sorter.py` |
| pydantic | 2.14.1 | `sorter.py` |
| python-dotenv | 1.2.4 | `hello.py`, `sorter.py` |
| fastapi | 0.143.3 | nothing yet (step 4) |
| uvicorn | 0.54.0 | nothing yet (step 4) |

## 4. Set up `.env`
Create a file named `.env` in the repo root with one line:
```
GEMINI_API_KEY=<your Gemini API key>
```
- Variable name: `GEMINI_API_KEY` (stated by Ayush).
- `load_dotenv()` loads `.env` into the environment. `genai.Client()` reads the key from there.
- The SDK also reads `GOOGLE_API_KEY`, and uses it over `GEMINI_API_KEY` if both are set. Seen in the installed `google-genai` source (`google/genai/_api_client.py`). Set only one.
- `.env` is in `.gitignore`. To check: `git check-ignore .env` prints `.env` if it is ignored.
- Never print, log, paste or commit the key.

## 5. Run
Activate the venv first: `source .venv/bin/activate`.

Step 1 smoke test (one Gemini call):
```bash
python hello.py
```
- Prints a short greeting from Gemini.
- Expect it to be slow. See `NUMBERS.md` and `GOTCHAS.md` #2.

Step 3 sorter, using the hard-coded sample dump:
```bash
python sorter.py
```
- Prints sections `== tonight ==`, `== this_week ==`, `== later ==`, `== cant_fix_now ==`.
- Each item is printed as `- <text>  (<why>)`.
- Then prints `Next step: ...` and `Took X.X s`.
- To try other text, change the `dump` string in the `__main__` block (`sorter.py:49–50`). Work-type tasks only (`GOTCHAS.md` #1).

## Not set up yet
- No FastAPI app, so there is no server to start yet (step 4).
- No HTML page (step 5).
- No tests and no test command.
