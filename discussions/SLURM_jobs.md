# Big SLURM Jobs

## 3/25/2025

## Attendance: 7

### Introduction

DSST members and friends gathered together to discuss our hard-earned tips and tricks on running big SLURM jobs. Big referred to both large numbers of jobs, see the biowulf [swarm documentation](https://hpc.nih.gov/apps/swarm.html), and jobs requiring high compute and memory resources.

### Tips and Tricks

While a variety of strategies were discussed, most of the experiences boiled down to:

1. Assume failure. [Murphy's Law](https://en.wikipedia.org/wiki/Murphy%27s_law#:~:text=Murphy's%20law%20is%20an%20adage,American%20aerospace%20engineer%20Edward%20A.) applies to your SLURM job. Even if you write your code perfectly, your prestine SLURM job can still fail if a squirrel chews through a power cable (yes, this actually happened at a university-run HPC). However, if you assume your code will fail, then you will be more inclined to incorporate some of the tatics below.

2. Logs. Logs. Logs. Monitoring the status of your job becomes much simpler if you use logs. Worried about parsing through a large log file? You can easily search a log file with [grep](https://www.gnu.org/software/grep/manual/grep.html), see the last few lines with [tail](https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html) (great for seeing where the job failed), or view it with a text editor.

3. Test using a subset. Most jobs DSST members and friends have to content with are iterative. Job that run the same script over many, many files. Before hitting ruturn on the big `sbatch` command, consider testing the full process on a small subset of jobs. Nothing is worse than running through your days long SLURM job to find that the final aggregation process had an error in it. Don't have a large number of files but a single large file to process? Consider running a test job on a scaled down version of the file. For large image files, you can process a subregion you crop out. Have timeseries data? Process a reasonable amount of timepoints.

4. Backup as you go. If you have a processing job that has multiple steps, consider writing out the intermediate derviatives to files to save time if you need to restart the job due to an errant squirrel. This is espesically true for parts of a pipeline that are compute intensive. If you don't know about the [pickle module](https://docs.python.org/3/library/pickle.html) or [numpy.save](https://numpy.org/devdocs/reference/generated/numpy.save.html) and [numpy.load](https://numpy.org/devdocs/reference/generated/numpy.load.html#), now may be a good time to click on those links. **If you write backup files be mindful of hard-drive space considerations! Use `/data`, 100 GB default, or `/scratch`, 100 TB shared but will get cleared space becomes limited.** See [Biowulf Storage Guide](https://hpc.nih.gov/storage/) for further details. Be sure to clear unnecessary files out when you are done! Depending on the size of your job, this may not be a feasible option without asking for more hard-disk space.

5. Track your completed files to save time on re-runs. If you have an iterative job, you may want to copy the processed files and their derivates to a different location. This will allow you to run the same job again, but skip the complete files detected in the "completed" directory. Alternatively, you can write out successful processing iterations in a log file, a CSV, or a database and have your re-run job skip the files already processed.

6. Beware zombie iterations due to external code failure. Let's say you are processing thousands of files in an analysis pipeline. You are a dedicated Python user, but one step in your pipeline requires a [subprocess](https://docs.python.org/3/library/subprocess.html) call out to some super efficient C++ code. Make sure you connect the output of that subprocess call to your Python script error handling. If the subprocess failed, make sure that bubbles up to kill your job or into your error logs. See `check_return_code` method of [CompletedProcess class](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess). Also, make sure you call `module load X` in your scripts if you need to rely on external code calls. Many modules must be loaded prior to use on biowulf!

7. Beware [race conditions](https://en.wikipedia.org/wiki/Race_condition). If you are parallalizing your job, make sure you have the derivative you need prior to running the code requiring it. To use a cooking metaphore, don't be in the middle of making a peach cobbler to discover you forgot the peaches. The concept of [mise en place](https://en.wikipedia.org/wiki/Mise_en_place) applies to parallarized SLURM jobs too.

8. Know thy code. Make sure you have a decent understanding of the time, compute, hard-drive space, and RAM memory requirements of your big SLURM job. This is usually accomplished by running a test set, see point 3 above.

### Job Monitoring

See biowulf docs on how to [Monitor Jobs](https://hpc.nih.gov/docs/userguide.html#monitor)

In addition, this alias may be useful to monitor for failed jobs. Consider adding it to your `.bashrc`

```bash
alias check_jobs='dashboard_cli jobs --since yesterday  --fields state,std_out,std_err | egrep "FAILED|TIMEOUT"'
```
