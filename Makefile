publish:
	python setup.py sdist upload

lint:
	@echo "Linting Python files"
	PYFLAKES_NODOCTEST=1 flake8 django_token
	@echo ""