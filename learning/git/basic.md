## Commands:
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

## The three trees
1. working - git add (stage) content
2. staging index - changes with added into staging to be committed
3. repository - git commit content

### SHA-1 algorithm to create checcksums - snapthot for the commit to keep data integrity (40 characters string)
### HEAD point to tip of curent branch in repository. Location .git/HEAD
### Untracked files - changes which are not in repository.
<br>

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
- git rm --cached file_to_ignore