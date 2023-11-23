# python-github-ci-pipeline
Example continuous-integration pipeline for a python project using GitHub actions and GitHub branch protection

<< **this repo is still under construction** >>

Implemented so far:

| Task                        | Location                | How to Run This Task
|-----------------------------|-------------------------|-----------------------------
| Auto-format all code scripts (uses [Ruff](https://github.com/astral-sh/ruff)) | local github repo | run in terminal: <code>make auto_format_code</code>
| Auto-format all code scripts (uses [Ruff](https://github.com/astral-sh/ruff)) | remote github repo      | runs automatically (using github action) whenever code is pushed to main branch
| Run all unit tests (including test coverage) | local github repo | run in terminal: <code>python -m pytest --verbose tests/unit --cov</code>

# Notes

* In order for GitHub actions to be able to write to the repository, you need to enable "Read and write permissions" on the GitHub website UI (Settings>>Actions>>General).

# Some Useful Resources 

* https://github.com/marketplace/actions/github-push