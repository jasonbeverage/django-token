publish:
	python setup.py sdist
	twine upload dist/*

lint:
	@echo "Linting Python files"
	PYFLAKES_NODOCTEST=1 flake8 django_token
	@echo ""