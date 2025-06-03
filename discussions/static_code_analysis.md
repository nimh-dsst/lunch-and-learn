# Static Code Analysis

3/18/2025, attendance: 8

## Quick Guide Resources

- [Ruff](https://docs.astral.sh/ruff/)
- [Ruff FAQ](https://docs.astral.sh/ruff/faq/)
- [Ruff Rules](https://docs.astral.sh/ruff/rules/)
- [Ruff Linter](https://docs.astral.sh/ruff/linter/)
- [Ruff Formatter](https://docs.astral.sh/ruff/formatter/)
- [Configuring Ruff](https://docs.astral.sh/ruff/configuration/)
- [Using Ruff with Editors](https://docs.astral.sh/ruff/editors/features/)
- [Setting up Ruff with VS Code](https://docs.astral.sh/ruff/editors/setup/#vs-code)

## Introduction

In today's Lunch and Learn, we discussed static code analysis in Python, focusing on linting, autoformatting, import sorting, and type checking. Many participants were introduced to static code analysis through tools set up by others, which can feel like magic incantations and be difficult to work with.

### Pros

- Automatically analyzes the codebase using rules or a style guide
- Flags issues early
- Enforces PEP8, the "official" Python style
- Improves code quality, readability, and maintainability
- Creates consistency across code
- Makes code reviews more efficient by focusing on content, not style
- Reduces bugs

### Cons

- Can be time-consuming
- Some tools do not play nice together
- Can be frustrating or buggy
- May feel like an obstacle

## Types of Checks and Common Tools

| Type         | Tool                        |
| ------------ | -------------------------- |
| Linter       | flake8, ruff               |
| Code style   | black, ruff                |
| Type checker | mypy, pyright              |
| Import order | isort, reorder-python-imports |

## Where to Run These Tools

| Run     | Purpose             | Tools           | Enforcement      |
| ------- | ------------------- | -------------- | --------------- |
| Locally | Preventative check  | pre-commit     | Can be skipped  |
| CI      | Validation check    | GitHub Actions | Can be enforced |

## Ruff

- 3-in-1 tool for linting, formatting and import sorting
  - Drop-in replacement for flake8, black, and isort
  - Note it is not a type checker!
- Super fast, written in Rust
- Implements over 800 [rules](https://docs.astral.sh/ruff/rules/)
  - Does not implement all Pylint rules (yet)

### Basic Usage

1. Format code with `ruff format`
2. Lint code with `ruff check`

- A unified command for both is [planned](https://github.com/astral-sh/ruff/issues/8232).

## Configuration

- For new projects, start with a basic configuration
- Ruff configuration parameters can be specified in the `pyproject.toml` or in the Ruff-specific `ruff.toml` file.
- By default Ruff does not enable the isort rules and flake8's complexity rule
- Many users only enable Flake8's F rules and a subset of E rules, omitting stylistic rules that overlap with formatters
- The most commonly changed settings are [line-length](https://docs.astral.sh/ruff/settings/#line-length) and [magic trailing comma](https://docs.astral.sh/ruff/settings/#format_skip-magic-trailing-comma)
- Note Ruff has different defaults than other tools
- Ruff checks and formats Jupyter notebooks by default ([more info](https://docs.astral.sh/ruff/faq/#does-ruff-support-jupyter-notebooks))

### Replicating Black Style

- Enable magic trailing comma
- Use double quotes
- Indent with spaces
- Line length 88
- Autodetect end of line
- Known [deviations](https://docs.astral.sh/ruff/formatter/black/) from Black
  - Formats f-strings
  - Differences in assert statements
- Configure import sorting with `profile = "black"` to replicate isort's behavior.

## Tips

- Decide which checks you need
- Choose where to run tools: locally, CI, or both
  - Long-running checks are better in CI, not pre-commit
- Pin dev tool versions to avoid unexpected CI/setup failures
  - Ruff uses a custom versioning scheme: minor = breaking, patch = bug fixes. No stable API yet. Once Ruff's API is stable, the major version number and semantic versioning will be used.
- Start with the default config
- Be mindful of which files are included in checks

## Tutorial Repo Coming Soon

- Check back for a link to a tutorial repo with examples

## Related Tools

- [uv](https://docs.astral.sh/uv/): manage Python projects, dependencies, and environments
- [pre-commit](https://pre-commit.com/): run checks locally; has an official GitHub Action
- [GitHub Actions](https://docs.github.com/en/actions): run checks on GitHub VMs
  - [Superlinter](https://github.com/marketplace/actions/super-linter): lints many languages/file formats
- [Ruff GitHub Action](https://github.com/astral-sh/ruff-action)
- [Dependabot](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide): auto-updates dependencies (not pre-commit hooks)
- [Renovate](https://docs.renovatebot.com/): auto-updates dependencies, including pre-commit hooks
