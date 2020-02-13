lint:
	black -l 79 --check .

type-check:
	find . -name '*.py' | xargs mypy --disallow-untyped-defs

test: lint type-check
