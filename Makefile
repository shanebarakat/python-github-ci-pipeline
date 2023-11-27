install_dev_dependencies:
	pip install -r requirements/build_docs.txt
	pip install -r requirements/clean_up.txt
	pip install -r requirements/tests.txt

install_prod_dependencies:
	pip install -r requirements/prod.txt

run_all_tests:
	make test_coverage linter type_checks

test_coverage:
	python -m pytest --verbose --cov

unit_tests:
	python -m pytest --verbose tests/unit

integration_tests:
	python -m pytest --verbose tests/integration

end_to_end_tests:
	python -m pytest --verbose tests/end_to_end

auto_format_full_codebase:
	ruff format .

linter:
	pylint diffie_hellman_merkle

type_checks:
	mypy diffie_hellman_merkle

check_docstring_example_code:
	python -m doctest diffie_hellman_merkle/helpers.py

view_docs_local:
	mkdocs serve

deploy_docs_to_github:
	mkdocs gh-deploy --force --clean --verbose