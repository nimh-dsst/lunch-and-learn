# Python Package Managers

## 2/4/2025

### Introduction

There are a [lot of options](https://chadsmith.dev/python-packaging/) (maybe [too many](https://dublog.net/blog/so-many-python-package-managers/)) for Python package managers, package builders, and dependency managers. Traditionally, [Conda](https://anaconda.org/anaconda/conda) has been used for package and dependency management in the life sciences, but there are other options. In this writeup of our Lunch and Learn discussion, we'll cover the following considerations for choosing a package manager:

- Purpose of the project
- End Users
- Setup complexity

### Purpose of the project

Selecting the right package manager depends on the purpose of the project. If the goal of the project is to create a single Python package for a small group of users, then a simple package manager like Python's  `pip` for dependency managment, `venv` for environment management, and `setuptools` (note `distutils` was deprecated in Python 3.10 and removed in Python 3.12) for building and distributing the package is sufficient.

However, more complex projects may benefit from package managers that provide addtional automation for building, testing, and distributing the package. Until recently, [Poetry](https://python-poetry.org/) was a popular choice for this purpose, but the new [UV](https://docs.astral.sh/uv/intro/) package manager is gaining traction. Recent DSST members have reported bugs in Poetry projects in recent weeks.

 These tools provide a lot of automation for managing dependencies, building, testing, and distributing the package. UV is written in Rust, which is a compiled language, so it is faster than pip and other Python package managers, provides lock-file support, and is compatible with existing Python projects such as the `pyproject.toml` file format. There is a [PyPI package](https://pypi.org/project/poetry-to-uv/) for converting Poetry projects to UV projects.

If a project requires custom binaries for execution or has multiple languages, then a package manager like Conda is a good choice. Conda is a package manager for any language, but it is particularly popular in the life sciences. Conda can be used to create an environment with the necessary dependencies to run the package. Recent additions to the Conda ecosystem are [mamba/micromamba](https://mamba.readthedocs.io/en/latest/) (a drop-in replacement for Conda) and [Pixi](https://prefix.dev/) which currently uses UV. With each claiming to be faster than Conda.

### End Users

If end users are not Python developers, then ease of installation is important. More automated tools like Conda or UV are better suited for this purpose, as they facilitate the installation of dependencies. However, if the end users are not technical, then the project may be better suited being placed in a containerized environment like [Docker](https://www.docker.com/)/[Podman](https://podman.io/) or [Singularity](https://sylabs.io/singularity/). Finally, if the end users are interested in learning Python, starting out with simple tools like pip and venv is a good way to demonstrate why they should use a more complex tool like Conda or UV as they get more comfortable with Python.

Note, while many end users are permitted to install Python, they may not be permitted to install Docker or Singularity. In this case, a package manager like Conda or UV is a good choice.

### Setup complexity

While a containerized application is easy to use, setting up the container can be complex depending on the system. For example, if the system does not have Docker or Singularity installed, then the user will need to install it. This can be a barrier to entry for some users lacking the expertise in containerization. Or Docker/Singularity may not be allowed by the system administrator.

Projects with multiple languages or custom binaries may have different setups based on the operating system. Conda is a good choice for this purpose, as it can be used to create an environment with the necessary dependencies to run the package. Less sophisticated tools like UV and pip will require setup of the other languages or binaries by the end users.

### Best Practices

- Always use virtual environments, regardless of the package manager chosen
- Document your environment setup (e.g., `environment.yml` for conda, `requirements.txt` for `pip`)
- Avoid mixing package managers within the same environment (especially conda and pip)
- Pin dependencies to specific versions for reproducibility
- Consider using lockfiles (poetry.lock, conda-lock, pip-compile) for deterministic builds
- Test environment creation from scratch regularly to ensure reproducibility

### Conclusion

There are a variety of factors that should be considered when choosing a package/dependency manager. Key considerations are whether the end users are technical or not, if the project requires multiple languages or custom binaries, and if the project goal is to provide a flexible environment or a containerized application.

| Manager | Pros | Cons | Best For |
|---------|------|------|-----------|
| pip+venv | Simple, built-in | Limited dependency resolution | Simple Python projects |
| Conda | Cross-language, robust | Slower, larger footprint | Complex scientific projects |
| UV | Fast, modern | Newer, less tested | Modern Python projects |
