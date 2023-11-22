install_dev_dependencies: requirements/dev.txt
	pip install -r requirements/dev.txt

install_prod_dependencies: requirements/dev.txt
	pip install -r requirements/prod.txt

run_all_tests:
	make unit_tests integration_tests linter type_checks

unit_tests:
	python -m pytest --verbose tests/unit --cov

integration_tests:
	python -m pytest --verbose tests/integration --cov

linter:
	pylint diffie_hellman_merkle

type_checks:
	mypy diffie_hellman_merkle