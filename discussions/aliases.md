# Aliases

## 12/4/2024

## Introduction to shell aliases

A shell alias is a shorthand or shortcut for a longer command that you frequently use in your terminal. Think of it as a nickname for a command or a combination of commands. Aliases can save you time and help prevent mistakes.

Aliases can be set on a shell instance by using the `alias` command. However, more users typically put alias commands in their shell's RC files. The RC files (RC is short for run commands), are run when a shell instance opens. These RC files are great for setting commonly used environment variables and aliases. For BASH shells, the RC is `~/.bashrc` and for ZSH shells, the RC is `~/.zshrc`. At NIH BASH is the default shell for Biowulf and Helix.

## Using an alias file

You may want to put all your additions into a separate file like ~/.bash_aliases, instead of adding them here directly. Just add the following to the RC file:

```bash
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```

## Example of Aliasing

## SSH'ing into servers

Let's say you have to log into several different servers. You can save time ssh'ing into them by aliasing the commands.

```bash
alias bw="ssh username@biowulf.nih.gov"
alias he="ssh username@helix.nih.gov"
```

Note you can achieve a simlar effect by shortening the name of the server in you SSH config file and adding in a default User.

```text
Host bw
  HostName biowulf.nih.gov
  User username
```

After editing the SSH config file the command would be `ssh bw`.

## Shortening long commands or frequently used commands

Below are few examples of Biowulf SLURM commands that are shortened using aliases.

```bash
alias sinteractive_small='sinteractive --mem=8G --cpus-per-task=4 --gres=lscratch:30'
alias sinteractive_medium='sinteractive --mem=16G --cpus-per-task=12 --gres=lscratch:100'
alias sinteractive_large='sinteractive --mem=24G --cpus-per-task=32 --gres=lscratch:150'
alias sinteractive_small_T='sinteractive --mem=6G --cpus-per-task=4 --tunnel'
alias sinteractive_small_lscratch='sinteractive --mem=6G --cpus-per-task=4 --gres=lscratch:50'
alias sinteractive_ml='sinteractive --mem=70G --cpus-per-task=20 --gres=lscratch:50 --gres=gpu:v100x:1'
alias swarm_call='swarm -f ./swarm.sh -t 10 -g 100 --partition gpu  --gres=gpu:v100x:1 --logdir=./logdir --time=10:00:00'
alias ll='ls -hltra'
alias lst='ls -1lt'
alias matlab='matlab -nosplash'
```

## Dedicated cd commands

When working on projects on remote servers it can be handy to create aliases to quickly navigate to those directories. Be sure to use absoluate directories so they work from anywhere.

```bash
alias cdproj='cd /data/scratch/username/root_project/subproject/'
```

## Typos

You can use alias for common misspellings of commands too!

```bash
alias histroy=history
alias hsitroy=history
alias shitroy=history
alias historuy=history
alias hisotry=history
alias hsitory=history
alias histyro=history
alias greo=grep
```

## Podman to docker

Podman is an open-source alternative to docker. However, many programs are written expecting docker to be installed and users can develop muscle memory over time for docker commands. Aliasing in an RC file allows for a seamless transition.

```bash
alias docker=podman
```

## A word of caution

While aliases can be great timesavers, they can affect a users understanding of how acutal commands work. The more aliases you use, the more you depend on those aliases in your muscle memory. If you use a lot of aliases, consider backing up your RC file.
