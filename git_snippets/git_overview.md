## Git overview

| Command                     | Description                                   |
| --------------------------- | --------------------------------------------- |
| git init                    | create a local repository                     |
| git add _file name_         | add file to repository                        |
| git add .                   | add all files to repository                   |
| git commit -m _'message'_   | create a snapshot of code                     |
| git status                  | see all done changes                          |
| git clone _repository path_ | clone remote repository on your local machine |
| git branch _branch name_    | create new branch                             |
| git checkout _branch name_  | change branch                                 |
| git push                    | push changes to branch                        |
| git merge _branch name_     | merge branches                                |

---

## Creating new repo algorithm

1. git init
2. git add .
3. git commit -m "first commit"
4. git branch -M main
5. git remote add origin https://github.com/*user_name*/*reposirory_name*.git
6. git push -u origin main
