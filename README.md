# python-github-ci-pipeline
Example continuous-integration pipeline for a python project using GitHub actions and GitHub branch protection

<< **this repo is still under construction** >>

Implemented so far:

| Task                        | Location                | How to Run This Task
|-----------------------------|-------------------------|-----------------------------
| auto-format all code scripts (uses [Ruff](https://github.com/astral-sh/ruff)) | local github repo | run in terminal (from project root folder):<br> <code>make auto_format_code</code>
| auto-format all code scripts (uses [Ruff](https://github.com/astral-sh/ruff)) | remote github repo      | task runs automatically (using github action) whenever code is pushed to main branch
| run all unit tests (including test coverage) | local github repo | run in terminal (from project root folder):<br> <code>make unit_tests</code>
| run code linting on core scripts in [/diffie_hellman_merkle/](./diffie_hellman_merkle/) folder (uses [Pylint](https://github.com/pylint-dev/pylint)) | local github repo | run in terminal (from project root folder):<br> <code>make linter</code>
| run static type checking on core scripts in [/diffie_hellman_merkle/](./diffie_hellman_merkle/) folder (uses [my[py]](https://github.com/python/mypy)) | local github repo | run in terminal (from project root folder):<br> <code>make type_checks</code>

# Setup Notes

* In order for GitHub actions to be able to write to the repository (e.g. to automatically format code, and then commit and push the changed code), you need to enable "Read and write permissions" for GitHub actions in the GitHub website UI (this is under *Settings>>Actions>>General*).

# Other Notes

* Remote rejections can be pre-empted by using [pre-commit](https://github.com/pre-commit/pre-commit) locally, which will cause commits of insufficient quality to be rejected locally when a <code>git commit</code> is attempted (i.e. before reaching the remote github repository). 

# Some Useful Resources 

* https://github.com/marketplace/actions/github-push