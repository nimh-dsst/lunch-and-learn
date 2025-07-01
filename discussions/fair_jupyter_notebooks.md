# Making Jupyter Notebooks F.A.I.R

## 6/17/2025, attendance 7

### Introduction

@joshlawrimore has a long-standing hatred of Jupyter Notebooks. Not because they have no value, on the contrary, they provide an excellent entry point for novice developers and analysts. No, @joshlawrimore hates it when he is handed a Jupyter notebook that isn't interoperable (the I in FAIR) nor reusable (the R).

### Interoperable

A key principle in software development is [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself#:~:text=%22Don't%20repeat%20yourself%22,redundancy%20in%20the%20first%20place.), don't repeat yourself. If you find yourself writing the same code over and over again, it should probably be a [function](https://www.w3schools.com/python/python_functions.asp). Functions should be defined at the top of a Jupyter Notebook or packaged together in separate `.py` files. These are called modules. You then import the functions at the beginning of the notebook. See [this guide](https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3) for more information.

For the best interoperability, consider publishing your requirements.txt or uv.lock/pyproject.toml file, your module files, and your notebook in a GitHub repo and packaging your module files into a Python package. See this [pyopensci.org guide](https://www.pyopensci.org/python-package-guide/tutorials/intro.html) for more information.

### Reusable

Ah, the convenience of a default Python environment. SageMaker has their default conda [environments](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab-environments.html). [Google CoLab](https://colab.research.google.com/) has their default. Simply run:

```python
!pip list
```

in a CoLab cell and see all those beautiful pre-installed packages. However, odds are you do not have a well-documented default Python environment. That means when the next person who runs your Jupyter notebook (probalby you in the future), they get to guess what packages and versions of packages you were using to get those results. So, please be kind to yourself and do one of the following:

#### Pip Freeze :snowflake:

Create a requirements.txt file using pip freeze. It's as simple as:

```bash
pip freeze >> requirements.txt
```

or, if you want to do it within the notebook, put

```bash
!pip freeze >> requirements.txt
```

in a notebook cell to produce the `requirements.txt` in the current working directory (usually the directory containing the notebook).

To install those packages on a new machine or virtual environment:

```bash
pip install -r requirements.txt
```

or in a notebook cell

```bash
!pip install -r requirements.txt
```

Keep that `requirements.txt` with your notebook in a GitHub repo and your future self will thank you.

#### UV

Here at DSST we :heart: [UV](https://docs.astral.sh/uv/). UV will automatically create a `uv.lock` file that has comprehensive documentation of package versions. This is a snapshot of what was used in that specific environment. It will also produce a list of packages in the `pyproject.toml` file. The `pyproject.toml` contains a list of dependencies with version constraints that are compatible with your code. The key difference is that pyproject.toml specifies version ranges that are compatible, while uv.lock pins the exact versions that were resolved. This allows for reproducible builds while maintaining flexibility for compatible updates.

Need to use Jupyter for something other than Python? Consider [mamba/micromamba](https://github.com/mamba-org/mamba) instead. Just be sure to export the environment into an `environment.yml` file using

```bash
mamba env export > environment.yml
```

that conda-lock.yml using [conda-lock](https://conda.github.io/conda-lock/)!

### Discussion

Jupyter notebooks are great for

- Demonstrating code usage
- Showing analysis results and graphs

Just make sure you can recreate those results and allow other researchers to easily reuse your code.
