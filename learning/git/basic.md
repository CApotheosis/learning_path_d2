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


.git - directory contains everything about project.

## The three trees
1. working - git add (stage) content
2. staging index - changes with added into staging to be committed
3. repository - git commit content

### SHA-1 algorithm to create checcksums - snapthot for the commit to keep data integrity (40 characters string)

### HEAD point to tip of curent branch in repository. Location .git/HEAD

### Untracked files - changes which are not in repository.

### View difference between commits
- `git diff` - to see changes different from current commit. difference between local and remote cahnges
- `git diff --staged` - difference between remote and local cahnges
