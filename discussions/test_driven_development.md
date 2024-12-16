# Test Driven Development

## 12/10/2024

## Introduction to Test Driven Development

Bob Martin, AKA [Uncle Bob](https://en.wikipedia.org/wiki/Robert_C._Martin) wrote a [blog post](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd) entitled "The Three Laws of TDD" that give a solid introduction to test driven development. They are:

- You are not allowed to write any production code unless it is to make a failing unit test pass.
- You are not allowed to write any more of a unit test than is sufficient to fail; and compilation failures are failures.
- You are not allowed to write any more production code than is sufficient to pass the one failing unit test.

## DSST Disucssion recap

DSST and friends discussed performing Test Driven Development in a biomedical research environment. The rough consensus among users was:

1. Writing good tests is challenging.
2. Writing challenging code benefits from good tests. So if the code really matters, write tests.
3. Getting data to test analysis code is difficult, especially if data has protected eletronic Patient Health Information (ePHI).

## Making Test Driven Development Easier

There are a variety of tools that make writing and running tests easier.

### Python Modules

Python has a built-in module called `unittest` that allows users to create a variety of testing scenarios. However, `unittest` has been critized for requiring too much boilerplate code and the third-party module `pytest` is often recommended instead.

- [unittest](https://docs.python.org/3/library/unittest.html)
- [pytest](https://docs.pytest.org/en/stable/)

### Visual Studio Code Integration

VS code has built in testing integration for both `unittest` and `pytest` when you install the [Python Extension](https://code.visualstudio.com/docs/languages/python). See the [testing docs](https://code.visualstudio.com/docs/python/testing)!

### GitHub Actions

Want to ensure that code updates don't break your codebase? Consider using [GitHub Actions](https://docs.github.com/en/actions) to automatically test your code. GitHub actions defines how compute nodes, called runners, test your code. GitHub-hosted runners are free but do have some RAM and storage limits. See [Supported runners and hardward resources](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/about-github-hosted-runners#supported-runners-and-hardware-resources) for more information.

### Getting Test Data

#### Sythetic data: Fake it to make it

What do you do if your data is either too big or private for public hosting using GitHub Actions? Make fake data! For example, lets say you are working with a large fluorescence image stack that is supposed to perform three dimensional segementation. Make a smaller NumPy array during testing with a known number of objects and test your code on the smaller dataset.

#### Existing Public Data

Don't want to generate your own data? Borrow data from a public hosted repository! Public data repositories like the [Dandi Archive](https://dandiarchive.org/) and [OpenNeuro](https://openneuro.org/) have data that is open to the public.
