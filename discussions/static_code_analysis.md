# Static code analysis

3/18/2025, attendance: 8

## Quick guide resources
- [Ruff](https://docs.astral.sh/ruff/)
- [Ruff FAQ](https://docs.astral.sh/ruff/faq/)
- [Ruff rules](https://docs.astral.sh/ruff/rules/)
- [Ruff linter](https://docs.astral.sh/ruff/linter/)
- [Ruff formater](https://docs.astral.sh/ruff/formatter/)
- [Configuring Ruff](https://docs.astral.sh/ruff/configuration/)
- [Using Ruff with editors](https://docs.astral.sh/ruff/editors/features/)
- [Setting up Ruff with VS code](https://docs.astral.sh/ruff/editors/setup/#vs-code)

## Introduction
In today's Lunch and Learn we discussed static code analysis with a focus on Python, including linting (flake8), autoformatting (black), import sorting (isort), and type checking (mypy). Many in the group were introduced to static code analysis by being forced to use tools previously setup by other people. It's viewed as magic incantation but can be difficult to work with.

### pros
- Automatically analyze the code base using a set of rules or a style guide
- Use static code analysis to flag issues
- Follow PEP8, the "official" Python style
- Improves code quality, readability, and maintainability
- Enforces a code standard, creating consistency
- Makes code reviews more efficient, focusing on actual contents of PR instead of linter/style changes
- Reduces the amount of bugs

### cons
- Can be time consuming
- Some tools do not play nice together
- Can be frustrating
- Can be buggy
- Can feel like an obstacle


## Types of checks and common tools

|type | tool |
| --- | --- |
| linter | flake8, ruff |
| code style | black, ruff |
| type checker | mypy, pyright |
| order imports | isort, reorder-python-imports |

## Where to run these tools

|run | purpose | tools | enforcement |
| --- | --- | --- | --- |
| locally | preventative check | pre-commit | can be skipped |
| CI | validation check | GitHub actions | can be enforced |

#### Examples
- CI validation check run with GitHub Actions
- Local preventative check run through uv
- Local preventative check run with pre-commit

## Ruff
- 3-in-1 tool, drop-in replacement for flake8, black and isort
- Super fast, written in rust
- Implements over 800 [rules](https://docs.astral.sh/ruff/rules/)

### Basic usage
1. Style code with `ruff format`
2. Lint code with `ruff check`
- Note a unified command for both linting and formatting is [planned](https://github.com/astral-sh/ruff/issues/8232).

### Differences with other tools
- Known [deviations](https://docs.astral.sh/ruff/formatter/black/) from Black.
- Doesn't currently implement all Pylint rules
- Ruff's import sorting is intended to be near-equivalent to isort's when using isort's profile = "black".
- Ruff formats f-strings
- Differences in assert statements

### Limitations
- Not a type checker!
- Not a drop in replacement (yet) for Pylint

## Configuration
- If you are just starting off with a new project and not switching from existing tools then it's recommended to start off with a basic config.
- ruff configuration can be stored in `pyproject.toml` or a separate ruff specific config file (`ruff.toml`)
    - Note each tool varies in how it's configured. For example, Black exclusively uses the `pyproject.toml` whereas flake8 does not support the `pyproject.toml`.
- Note ruff has different defaults compared to other tools
- isort rules are not implemented by default
- Most commonly changed parameters are line length and trailing magic comma.
- By default ruff does not implement flake8 complexity rule.
- Many add Flake8's F rules, along with a subset of the E rules, omitting any stylistic rules that overlap with the use of a formatter, like ruff format or Black.
- By default ruff will check/format Jupyter notebooks. See [link](https://docs.astral.sh/ruff/faq/#does-ruff-support-jupyter-notebooks) for more info.

#### Replicating Black style
- Enable magic trailing comma
- Double quotes
- Indent spaces
- Line length 88
- Autodetect end of line

## Tips
- What checks do you want to do?
- Where do you want to run these tools? What is the runtime environment?
    - locally (preventative check), CI or both
    - If they are long running checks they are better to run exclusively in CI and not with pre-commit
- Pin the versions of dev tools to ensure setup/CI does not unexpectedly fail.
    - Note Ruff uses a custom versioning scheme that uses the minor version number for breaking changes and the patch version number for bug fixes. Ruff does not yet have a stable API; once Ruff's API is stable, the major version number and semantic versioning will be used.
- Start with the default config
- Be mindful of what files are being included in the checks

## Tutorial repo coming soon!
- Check back for a link to a tutorial repo with examples

## Tangentially related tools
- [uv](https://docs.astral.sh/uv/) (manage python projects, dependencies and environments)
- [pre-commit](https://pre-commit.com/) (facilitates running checks locally)
    - also has an official GitHub action
- [Github Actions](https://docs.github.com/en/actions) (facilitates running checks on a GitHub hosted VM)
    - [Superlinter](https://github.com/marketplace/actions/super-linter) (GHA to lint nearly(?) all languages/file formats)
- [Ruff GitHub Action](https://github.com/astral-sh/ruff-action)
- [Dependabot](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide) (automatically update project dependencies)
    - Does not update `pre-commit` hook versions
- [Renovate](https://docs.renovatebot.com/) (automatic dependency updates, including pre-commit hooks)
