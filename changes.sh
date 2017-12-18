# git log 1.0-RC1.. --pretty=format:'- [%s](http://github.com/citation-file-format/citation-file-format.github.io/commit/%H)' --reverse | grep -v Merge > changes.md
# git log src... --pretty=format:'- [%s](http://github.com/citation-file-format/citation-file-format.github.io/commit/%H)' --reverse | grep -v Merge > changes.md
git log --boundary --no-merges --pretty=format:'- [%s](http://github.com/citation-file-format/citation-file-format.github.io/commit/%H)' --reverse src..HEAD | grep -v Merge > 1.X.X-CORRECT-VERSION-HERE-changes.md

# Use in Python script for every dir that contains a specifications.md