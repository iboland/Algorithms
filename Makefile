lint:
	black -l 79 --check .
	find . -name '*.py' | xargs mypy --disallow-untyped-defs
