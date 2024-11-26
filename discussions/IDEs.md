# Interactive Development Environments (IDEs) Discussion

## IDEs used by Data Science and Sharing Team and Friends

* [VS Code](https://code.visualstudio.com/)
* [PyCharm](https://www.jetbrains.com/pycharm/). There is a free Community Edition and a Professional Edition. Scroll down for Community Edition on the [downloads page](https://www.jetbrains.com/pycharm/download/). Also see definition of [Dark Pattern](https://en.wikipedia.org/wiki/Dark_pattern) in web design.
* [Spyder](https://www.spyder-ide.org/)
* [Cursor](https://www.cursor.com/)
* [Positron](https://positron.posit.co/). "A next-generation data science IDE built by [Posit PBC](https://posit.co/)"
* [Sublime Text](https://www.sublimetext.com/)
* [emacs](https://www.gnu.org/software/emacs/)

## IDE considerations

During the discussions users brought up pros and cons of various IDEs. Here are some of the highlights:

### Git Integration

Most IDEs offer GUI interfaces for common git actions. However, some users prefered using git from the command line instead.

### VS Code Considerations

* VS Code's [testing interface](https://code.visualstudio.com/docs/editor/testing) provides support for Python's `unittest` and `pytest`.
* Extensions in VS Code
  * [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) by Microsoft
  * [GitHub Pull Requests Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
  * [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
  * [Flake8](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)
  * [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)
  * [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot). Requires a paid subscription.
  * [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat). Requires a paid subscription.

### Do you need to see the data?

An interesting point of discusssion was raised about whether or not users preferred to see the data. Spyder comes with a variable explorer panel. Jupyter notebooks facilitate pandas DataFrame visualizations and plotting. For Data Science and Analytics tasks, sometime a faciliated view into the data can be helpful. Sometimes it is helpful to be able to traverse tabular data in Excel.

### AI-enabled IDEs

Both Cursor and GitHub Copilot Chat allow for users to ask high-level questions about code repositories. A user of Copilot found that hallucinations can occur, but still found massive value in code completion and automated doc-string writing. The quality of the code written by LLMs was likened to a junior developer or the old use of the term "corporate" to describe something devoid of style.

## Other Useful Topics

### Pandas query method

Faster to write than a `loc` statement: see [Pandas docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html) on the `query` method.

### Polars

Users didn't have much experience with the up-and-coming library but there was definite interest. There is an online [Meetup](https://www.meetup.com/mke-python-meetup/events/304631987/?recId=e1eb00fe-ef90-4626-a71c-c98a098fd651&recSource=keyword_search&searchId=2bcfc3d6-b280-435a-8846-7c9a0338a025&eventOrigin=find_page$all&_gl=1*c3x9hp*_up*MQ..*_ga*NTU1MTk0NjA2LjE3MzI2NDQzNjI.*_ga_NP82XMKW0P*MTczMjY0NDM2Mi4xLjAuMTczMjY0NDM2Mi4wLjAuMA) discussing Polars on December 3rd, 2024.

### Code Documentation

There was a brief disussion on making and hosting code documentation. Eric has experience with [MkDocs](https://www.mkdocs.org/) which produces static webpages that can be hosted on [GitPages](https://pages.github.com/) or [ReadTheDocs](https://about.readthedocs.com/). An alternative solution was [Jupyter Book](https://jupyterbook.org/en/stable/intro.html).
