# Code Debugging

## 4/15/2025

Attendence: 5

### Introduction

DSST Members and friends discussed debugging practices and code quality resources for scientific programming.

### Python Debugger - Breakpoints

When trying to decipher what a large analysis pipeline is doing, it can be helpful to monitor the status of the variables as it traverses the pipeline. Using breakpoints in the Python Debugger is a great way to keep track of how the code processing the data. However, one gotcha of the Python Debugger in VS Code/Cursor is that the code does **NOT** stop at breakpoints in third-party libraries by default. To enable breakpoints in third-party code, you must create a `launch.json` and run the debugger using those settings.

To create a `launch.json` file using the VS Code graphical interface:

1. Open the Python script you want to debug.
2. Click the dropdown arrow next to the "Run" button (usually a play icon) in the top-right corner of the editor.
3. Select "Run and Debug" from the dropdown menu.
4. If prompted, choose the "Python" debugger configuration (e.g., "Python File").
5. VS Code will automatically create a `.vscode` folder in your workspace root (if it doesn't exist) and add a `launch.json` file with a default Python debugging configuration. The file will open, allowing you to customize the settings, such as enabling `justMyCode: false` to step into third-party libraries.

Note, MATLAB also has breakpoints funcitonality. For more on Python Debugging in VS Code see [these docs](https://code.visualstudio.com/docs/debugtest/debugging). For MATLAB, see [these docs](https://www.mathworks.com/help/matlab/matlab_prog/debugging-process-and-features.html).

### Debugging Analysis Pipelines

During the discussion DSST members and friends shared common ways for debugging data pipelines.

- Visualize the data. Finding data anomalies can be difficult by just looking at variables directly. However, directly plotting or visualizing the data can make anomaly detection much easier. **A picture is worth a thousand words!**
- Check data types and shapes. When things go sideways in data pipelines, you can sometimes detect them by checking the shape or type of the data. If you are expecting a 256x256 binary mask and you get a linear numpy array of complex values, things have gone very very wrong. If you are writing custom pipelines, consider a data validation tool, like [Pydantic](https://docs.pydantic.dev/latest/).
- Run a known dataset through the pipeline. When debugging an analysis pipeline, starting with clean data eliminates the possiblity that the data is the issue. Sometimes the code is fine and the data is the problem. Consider keeping toy or dummy datasets for this purpose. Using a testing framework, like [PyTest](https://docs.pytest.org/en/stable/), can make this much easier.
- If the pipeline generates logs, check the logs. If the pipeline doesn't have logs, consider adding logs to help debugging. Here is a [Real Python article](https://realpython.com/python-logging/) and a [GeeksforGeeks article]( https://www.geeksforgeeks.org/logging-in-python/) on using Python's Logging module.

### Coding Resources

As is our wont during these discussions, DSST member and friends shared some of their favorite resources for scientific programming.

- [Good enough practices in scientific computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510). See Box1
- [The Good Research Code Handbook](https://goodresearch.dev/)
- [Scientific Python Cookiecutter](https://nsls-ii.github.io/scientific-python-cookiecutter/guiding-design-principles.html)
