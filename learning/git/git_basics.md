Themes:
1. Git history
    1. previous VCS's and Git
    2. git help
2. Getting started
    1. git init
    2. where Git files are stored
    3. first commit
    4. write commit message
    5. view commit log
    6. Quiz
3. Git concepts and architecture
    1. a
4. Make changes to Files
    1. a
5. Use Git with Real projects
    1. a
6. Undo changes
    1. a
7. Ignore files
    1. a


## Git history
Git is a version control system (VCS) which is distributed and can me locally managed with all the updates user applies to his/her project

First version control system:
1. Source Code Control System (SCCS)
```
What SCCS does is it keeps the original document, but then instead of saving the whole document a second time, it just saves a snapshot of what the changes were. So if you want version five of a document, you just take version one and apply four sets of changes to it to get to version five.
```
2. Revision Control System (RCS)
```
with RCS we can bring changes to a file in any given version, on contrary SCCS need us to have original file and apply all the snapshot changes before accessing other version and that's why it's a lot more faster. Both of these vcs allow to work only with a single file.
```
3. Concurrent Version System (CVS)
```
CVS allowed us access and work with multiple files and allowed to store our code on remote server, which allowed others to work on the same file at the same (before we couldn't do that)
```
4. Apache Subversion (SVN)
```
The idea of working with remote repositories was further improved upon with an Apache Subversion or SVN for short. SVN allowed to save non-text files like images. The biggest innovation was that SVN was keeping track of changes as a whole, meaning it keeped the state of whole directory. Watching files and directories collectively and actually taking a snapshot of the directory, not just the files.

In CVS, we could talk about having version seven of some files. In SVN, we discussed having that file, as it appears in revision seven. SVN was able to track the history of directories. For example, CVS had a hard time if you renamed a file. SVN though would track that change with no problem. If you add a file, remove a file, or rename it, it's watching the directory as a whole to see what happens and taking a snapshot of that where CVS was just looking at a collection of individually named files. CVS would also update files one at a time as it went to either apply or read back changes. SVN would instead do that transactional commit and apply all of the changes that happened to the directory or to none of them at all. The snapshot was bigger than just the individual files. It was an entire directory or an entire set of changes that were happening to that directory at one time. It's a subtle but important difference. 
```
5. BitKeeper (commercial) and Git (opensource) distributed version control systems
```
We looked at the history of version control systems, we talked about SCCS, RCS, CVS and SVN, four of the most popular version control systems of the past but all four of these use a central code repository model. That's where one central place is used to store the master copy of your code.

Git doesn't work that way. Git really focuses on these change sets and encapsulates a change set as a discrete unit, and then those change sets can be exchanged between repositories. We're not trying to keep up to date with the latest version of something. Instead, the question is do we have a change set applied or not? So you might say that you merge in change sets or you apply patches between the different repositories. So there's no single master repository. There's just many working copies, each with their own combination of change sets. Let me give an illustration to make this point clear. Imagine that we have changes to a single document as sets A, B, C, D, E, and F. We're just going to give them arbitrary letter names so that we can help see it. We could have a first repository that has all six of those change sets in it. We can have repository two that only has four of those changes in it. It's not that it's behind repository one, or that it needs to be brought up to date.

Tell about forking and working with between different repositories.
```
`git help` and it's usage.






In previous versions of version control system


## 1. Getting started
Git levels:
1. System
2. User
3. Project

### Configuring git (windows)
- user folder ~/.gitconfig file that stores configuration globally
- project configuration folder project/.git/config
### Configuration can be set according to level:
1. System: git config --system
2. Use: git config --global 
3. Project: git config

### Initializing git:
- `git config --global user.name "name in github"`
- `git config --global user.email "realemail"`

`git config --list`: выводит все настройки конфигурации

`git config user.name`: чтобы вывести определенную конфигурацию

`git config --global core.editor` - to set editor to open
```
Мы можем менять/обновить/создать конфигурацию прямо в .git
```

### Commands:
- `ls -la` - shows hidden file
- `git add .` - adds all changes
- `git commit -m` "Message to commit with" - commits added changes
- `git log` - returns history of all commits from current branch
- `git log -n 5` - returns 5 last commits
- `git log --since=2019-01-01`
- `git log --until=2019-01-01`
- `git log --author="Author name"`
- `git log --grep="Commit message to search"`
- `git status` - check for changes in project from current status
- `git commit -a` (--all) - stages and commits at the same time
- `git commit -am "Message to commit with"`

.git - directory contains everything about project.

## 3. Git concepts and architecture
### The three trees
1. working - git add (stage) content
2. staging index - changes with added into staging to be committed
3. repository - git commit content

### SHA-1 algorithm to create checcksums - snapthot for the commit to keep data integrity (40 characters string)
### HEAD point to tip of curent branch in repository. Location .git/HEAD
### Untracked files - changes which are not in repository.
<br>

## 4. Make changes to Files 
### View difference between commits
- `git diff` - to see changes different from current commit. difference between local and remote cahnges
- `git diff --staged` - difference between remote and local cahnges
- `git diff --color-words` - colors changes only
- `git diff commit_one_hash..commit_two_hash` - comparing commits. we can use HEAD to point to last commit

### Deleting files
- delete from filesystem
- git rm file_to_delete - delete file permanently from local and add to staging 

After renaming file locally, if the file content is 50% similar to older version, git will says its renamed, else it's deleted for git.
If we apply changes with filesystem, git won't track changes as it is. Id we do it from commands line it will.

## Atomic commits
- small commits
- only affect a single aspect
- easier to understand, to work with, and to find bugs
- improves collaboration


## Undoing changes
- git checkout -- file_to_undo_changes_from: -- is for returning state of the file/directory to the ones before change

## Unstaging files
- git add tours* - add all that start from tours
- git reset HEAD change_to_unstage

## Amending commits
- git commit --amend - rewrite current commit with new one, without creating new commit.

## Retrieve old version
- git checkout commit_sha-1 -- file_return_changes_from
- git diff --staged - to see changes
- git reset HEAD file_to_reset - unstage file(s)
- git checkout -- file_to_reset - sets it as a current file version

## Revert commit
- git revert hash_of_the_commit - reverts commit to current stage
- there might be merge conflicts necessary to resolve

## Remove Untracked Files - to remove many files from repository
- git clean [OPTIONS]: 
    - -i - interactive mode
    - -n - print message of the action (will print the list of files which is not in repository)
    - -f - will remove files permanently


## Questions
- What is the difference between git reset HEAD header.c and git checkout -- header.c? 
    - option - git reset changes the staging index and git checkout changes the working directory. 
    - answer - git reset HEAD unstages files, or removes the changes from the staging index, while git checkout pulls the last commit's version of a file from the repository and replaces the working directory version with it.

# Ignoring files
## Pattern matching
-  `* ? [aeiou] [0-9]`
- `logs/*.txt`
## Negative expressions
- `*.php` - ignore all files
- `!index.php` - do not ignore index.php 

## Gloabally ignore files
- git config --global core.exclidesfile ~/.gitignore_global - ignores files globally

## Ignore tracked files
- git rm --cached file_to_ignore - unstages file from remote repository


## Track empty directories
create .gitkeep file inside an empty directory