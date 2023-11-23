install_dev_dependencies: requirements/dev.txt
	pip install -r requirements/dev.txt

install_prod_dependencies: requirements/dev.txt
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
	python -m pytest --verbose tests/test_end_to_end.py

auto_format_code:
	ruff format .

linter:
	pylint diffie_hellman_merkle

type_checks:
	mypy diffie_hellman_merkle