install_dev_dependencies:
	pip install -r requirements/dev.txt

install_prod_dependencies:
	pip install -r requirements/prod.txt

run_tests:
	python -m pytest --verbose