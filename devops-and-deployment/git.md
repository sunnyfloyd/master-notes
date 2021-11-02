# Git

## Table of Content

- [Git](#git)
  - [Table of Content](#table-of-content)
  - [GitHub Usage](#github-usage)
  - [General](#general)
  - [Branch Management](#branch-management)
    - [Creating repo first/using existing repo](#creating-repo-firstusing-existing-repo)
    - [Starting local repo and then publishing it to GitHub](#starting-local-repo-and-then-publishing-it-to-github)
  - [Diff](#diff)
  - [Log](#log)
  - [Merging](#merging)
  - [Tags](#tags)
  - [Remote Repos](#remote-repos)
  - [GitHub Actions](#github-actions)

## GitHub Usage

There are two primary ways people collaborate on GitHub:

  - Shared repository
  - Fork and pull

- With a **shared repository**, individuals and teams are explicitly designated as contributors with read, write, or administrator access. This simple permission structure, combined with features like protected branches and Marketplace, helps teams progress quickly when they adopt GitHub.

- For an open source project, or for projects to which anyone can contribute, managing individual permissions can be challenging, but a **fork and pull model** allows anyone who can view the project to contribute. A fork is a copy of a project under an developer’s personal account. Every developer has full control of their fork and is free to implement a fix or new feature. Work completed in forks is either kept separate, or is surfaced back to the original project via a pull request. There, maintainers can review the suggested changes before they’re merged.

## General

- Checking the username ```git config --global user.name "your name goes here"```.

- After creating a new directory a Git repository initialization is done via ```git init```.

- Repo status is checked with ```git status```.

- Adding a file to the stage so changes to the file will be ready for the next commit ```git add file_name```.

- Commiting ```git commit -m "commit message"```.

- To stage and commit all of the files with changes use `git commit -am "commit message"` (this applies only to the files that have already been added before).

- Within a *.gitignore* file list of files/folders to be ignored by Git can be provided:

```bash
# .gitignore
__pycache__
venv
env
.pytest_cache
.coverage
```

- Within Git only source files should be stored - not the output files or large binary files (binary files do not have good diff tools so most of the time they will have to be stored fully each time they are committed).

- *SHA* is an unique (most likely) identifier of a commit in a given repository whereas a *HEAD* indicates on what commit I am currently working on.

- Instead of using *SHAs* to move between commits refs can be used:

```bash
git switch HEAD^  # switches to the parent of HEAD
git switch HEAD~3  # switches to the great great grandparent of HEAD
```

- `git branch` will list all of the branches in the repository and will mark the currently used one.

- ```git checkout <SHA>``` or ```git switch <SHA>``` switches between the commits. In order to get back to the origin use ```git checkout master/main```.

- If any changes are made when *HEAD* is detached those can be saved using ```git checkout -b <new-branch-name>``` or with a new syntax ```switch -c <new-branch-name>```.

- ```git checkout -b <new-branch-name>``` creates a new branch to work on (*b* flag indicates that we want to create a **new** branch). New branch starts at the location *HEAD* was currently at.

- To compare branches together use ```git show-branch <first-branch> <second-branch>```. If instead of labels you want to see *SHAs* use ```git show-branch --sha1-name <first-branch> <second-branch>```

- To revert a file to its state from the last commit use `git checkout <file_name>`.

- `git reset --hard HEAD` throws away any uncommitted changes.

## Branch Management

- To fetch all the remote branches from the repository `git fetch origin`.

- To see the branches available for checkout `git branch -a`.

- You cannot make changes directly on a remote branch. Hence, you need a copy of that branch. To copy the remote branch *fix-failing-tests*: `git checkout -b fix-failing-tests origin/fix-failing-tests`.

### Creating repo first/using existing repo

- When you create a branch locally, it exists only locally until it is pushed to GitHub where it becomes the remote branch:

```bash
git clone [repo_URL]
cd repo
# create a new branch
git branch new-branch
# change environment to the new branch
git checkout new-branch
# create a change
touch new-file.js
# commit the change
git add .
git commit -m "add new file"
# push to a new branch
git push --set-upstream origin new-branch
```

### Starting local repo and then publishing it to GitHub

```bash
# create a new directory, and initialize it with git-specific functions
git init my-repo

# change into the `my-repo` directory
cd my-repo

# create the first file in the project
touch README.md

# git isn't aware of the file, stage it
git add README.md

# take a snapshot of the staging area
git commit -m "add README to initial commit"

# provide the path for the repository you created on github
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

# push changes to github
git push --set-upstream origin main
```

## Diff

- `git diff` - difference between working tree and staging area (unstaged changes).

- `git diff --staged` - difference between staged changes and the most recent commit.

- `git diff HEAD` - difference between working tree and HEAD commit.

## Log

- ```git log``` shows history of all the commits that have been made up to this point.

- `git log --oneline` provides a list of commits with commit ref and commit message.

- `git log --stat` provides additional information about files changed in each commit, number of lines changed (additions/subtractions).

- `git log --patch` shows actual difference of each subsequent commits.

- `git log --patch --oneline` to combine oneliner with patch info.

- `git log --graph --all --decorate --oneline` shows one-line summary for each commit, ASCII art graphs all of the commits with their flow and their branches.

## Merging

- There are three main ways to combine commits from two different branches:

  1. **Merging** - from the master branch (or any other to which we want to merge changes) ```git merge <branch-name>```.
  2. **Rebasing** - similar to merging - if both branches have commits then a new *merge commit* is created: ```git rebase <base_branch> <branch_to_be_rebased>```.
  3. **Cherry-picking** - you specify exactly which commits (using their *SHAs*) you mean to merge with the master ```git cherry-pick <SHA_ID>```.

- **Cherry-picking** is a way of copying certain commits to HEAD: ```git cherry-pick <Commit1> <Commit2> <...>```.

- **Interactive rebase** allows for picking exact commits and their order that will be picked to indicated location ```git rebase -i HEAD~3```.

- If changes need to be done to an earlier commit without changes to the commit flow (commit tree) following can be done:

  - re-order the commits so the one we want to change is on top with ```git rebase -i```,
  - ```git commit --amend``` to make the slight modification,
  - re-order the commits back to how they were previously with ```git rebase -i```.

- Above can be done using ```git cherry-pick```:

  - get to the desired branch and cherry-pick commit that requires changes,
  - amend cherry-picked change,
  - cherry-pick all of following commits to get the previous order.

- To move branch to the other commits ```git branch -f main HEAD~3``` can be used.

- To delete a branch `git branch -d <branch_name>` - this is especially useful when some bug fixing/new feature development has happened on a new branch and master branch has already been merged with such branch so it can be deleted.

## Tags

- To permanently mark a certain commit as a milestone that can be referenced like a branch but cannot be move to other commits use: ```git tav tag_name [tag_location (default is HEAD)]```.

- Because tags serve as such great "anchors" in the codebase, git has a command to describe where you are relative to the closest "anchor" (aka tag). And that command is called `git describe`!

## Remote Repos

- Usual path to contribute to other's projects: fork repository -> clone -> make changes -> commit -> pull request.

- To reset **local** changes use ```git reset HEAD``` - this will *change history* by reverting branch backwards as if the commit had never been made in the first place.

- To revert changes in the remote branches use ```git revert HEAD```.

- Working with remote repos:

  - cloning a repo: ```git clone git@github.com:sunnyfloyd/python-learning-points-and-improvements.git``` OR add remote repo with `git remote add name-of-repo https://github.com/me50/sunnyfloyd.git OR userna5@desination:/home/userna5/production.git`;
  - checking whether remote repo is already configured: ```git remote -v```;
  - configuring remote repo: ```git remote add <remote_stream_name> https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git```;
  - OPTIONAL (if assigning local git repo to a remote one instead of cloning): `git push --set-upstream <remote_stream_name> <branch name (master)>`. This might also need configuring on the branch level as well: `git branch --set-upstream-to=<remote_upstream>/<remote_branch> <local_branch>`;
  - fetching (retrieving latest meta-data info from the online repo) a repo: ```git fetch```;
  - pulling (combination of ```fetch``` and ```merge``` since it actually brings copy of eventual changes from the remote repo): ```git pull```;
  - pushing: ```git push```.

## GitHub Actions

- **Continous Integration**
  - frequent merges to main branch
  - automated unit testing

- **Continous Delivery**
  - short release schedules

- **GitHub Actions** will allow us to create workflows where we can specify certain actions to be performed every time someone pushes to a git repository. For example, we might want to check with every push that a style guide is adhered to, or that a set of unit tests is passed.

- Github Actions uses **YAML** to specify the CI workflow:

```YAML
# In .github/workflows/ci.yml
name: Testing
on: push

jobs:
  test_project:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Run Django unit tests
      run: |
        pip3 install --user django
        python3 manage.py test 
```
