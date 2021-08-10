**Related issues**

Refs: #ISSUE_NUMBER

(For autoclosure of issues when PR is merged use `Fixes #<issue-number>` syntax)

**Describe the changes made in this pull request**

**Instructions to review the pull request**

- [ ] **Reviewers** Please check if all changes are recorded in `CHANGELOG.md` and adapt if neccesary.
- [ ] **Contributors:** Please replace `<do other things>` in the snippet below with something that reviewers should do to test and review your contribution!
```bash
cd $(mktemp -d --tmpdir cff.XXXXXX)
git clone https://github.com/citation-file-format/citation-file-format .
git checkout <branch>
python3 -m venv env
source env/bin/activate
pip install --upgrade pip wheel setuptools
pip install -r requirements.txt
pytest
<do other things>
```
- [ ] **Contributors:** Please add anything else that should be done here ...
