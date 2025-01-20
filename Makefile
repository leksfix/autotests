lint:
	uv run ruff check .

build:
	uv build

test:
	PYTHONPATH=mypackage python3 tests/test_capitalize.py

package-install:
	uv tool install --force-reinstall dist/*.whl
