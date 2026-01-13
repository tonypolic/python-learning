# Copilot / AI Agent Instructions — python-learning

Purpose
- Help AI coding agents be immediately productive in this small, educational Python repo.

Big picture
- This repository is minimal: core code lives under `basics/` as standalone scripts used for learning. There is no package, tests, or CI in the repo.
- Key files: `basics/hello.py`, `basics/input_example.py`, `basics/variables.py` — read these together to understand project intent (beginner-focused examples, short procedural scripts).

What to preserve
- Preserve the pedagogical intent: changes should keep examples simple and explicit. Avoid introducing frameworks or advanced idioms unless the change is explicitly educational.
- Preserve any user-visible strings (examples and prompts) unless asked to reword them for clarity.

Developer workflows (how to run and debug)
- Run a script directly: `python basics/hello.py` (same for other files).
- Use a REPL to experiment with small edits: `python -i basics/hello.py` or run the file inside an IDE debugger.

Project-specific patterns and conventions
- Single-file scripts: prefer minimal, self-contained edits. If you add helper functions, keep them in the same file unless consolidating multiple examples.
- No external dependencies: don't add packages unless a user requests expanded examples with dependencies and a `requirements.txt` is added.

Examples of common, acceptable edits
- Fix obvious syntax/runtime errors and make error messages beginner-friendly.
- Improve comments and short inline explanations to make learning clearer.
- Add small, self-contained examples (<= 30 lines) that illustrate a single concept.

What to avoid
- Do not convert the repo into a package or introduce a build system without explicit instruction.
- Do not remove or significantly rewrite example prompts or sample inputs unless requested.

Integration points and external dependencies
- None by default. If a change introduces external libraries, include a `requirements.txt` and update these instructions.

If unsure
- Ask a human for guidance when a change would expand the repo's scope (adding tests, CI, packaging, or external services).

Files to inspect for context
- `basics/hello.py` — entry-level example (first read this).
- `basics/input_example.py` — demonstrates input handling and prompts.
- `basics/variables.py` — shows variable usage and simple expressions.

Contact
- Leave a short PR note explaining why a non-trivial change helps the learning goals (what concept it teaches or how it simplifies learning).
