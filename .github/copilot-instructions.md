# Copilot / AI Agent Instructions — python-learning

## Purpose
Help AI coding agents be immediately productive in this small, educational Python repo for beginner Python learning.

## Architecture
This repository is minimal and intentionally simple:
- **Core code**: Standalone scripts under `basics/` folder (no packages, no tests, no CI)
- **Entry-level flow**: `hello.py` → `variables.py` → `input_example.py` (read in this order to understand scope)
- **Scope**: Procedural scripts demonstrating fundamental concepts: output, variables, input/types

## Critical Developer Workflows
- **Run scripts**: `python basics/hello.py` (or any file in `basics/`)
- **Interactive testing**: `python -i basics/hello.py` for REPL experimentation with small edits
- **IDE debugging**: Use VS Code debugger to step through any single file

## Project-Specific Patterns & Conventions
- **Single-file scripts**: Keep edits minimal and self-contained. If adding functions, keep them in the same file unless consolidating multiple examples.
- **Pedagogical purity**: Preserve simplicity and explicitness. Avoid frameworks, decorators, or advanced idioms unless explicitly educational.
- **No external dependencies**: All examples use only Python stdlib. If expansion requires packages, create `requirements.txt` and document in these instructions.
- **User-visible strings**: Preserve example prompts/outputs unless asked to reword for clarity.

## Discoverable Patterns from Files
- **hello.py**: Multilingual `print()` example (currently prints Greek text)
- **variables.py**: Basic assignment with simple types (str, int) and print statements
- **input_example.py**: Interactive prompts with `input()`, string concatenation, f-strings, `len()`, type conversion, arithmetic

## Acceptable Edits
- Fix syntax/runtime errors with beginner-friendly messages
- Improve inline comments and explanations
- Add small examples (≤30 lines) teaching a single concept
- Clarify variable names or output text

## What to Avoid
- Do not convert to a package or add build systems without explicit instruction
- Do not remove or rewrite example prompts unless requested
- Do not introduce external dependencies without user consent and `requirements.txt`
- Do not use advanced features (decorators, metaclasses, comprehensions beyond basics)

## Integration & Dependencies
- None by default; pure Python stdlib only
- Ask user before adding any external library

## If Unsure
Ask for human guidance when changes would expand scope (tests, CI, packaging, external services).
