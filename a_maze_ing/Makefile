.PHONY: install run debug clean lint lint-strict build

# Install project dependencies [cite: 85]
# install:
# 	pip install flake8 mypy wheel setuptools
# Install project dependencies
install:
	python3 -m pip install flake8 mypy wheel setuptools

# Execute the main script of your project [cite: 86]
run:
	python3 a_maze_ing.py config.txt

# Run the main script in debug mode using Python's built-in debugger [cite: 87]
debug:
	python3 -m pdb a_maze_ing.py config.txt

# Remove temporary files or caches to keep the project environment clean [cite: 88]
clean:
	rm -rf __pycache__ .mypy_cache build dist mazegen.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -f *.whl *.tar.gz

# Execute the required linter commands [cite: 91, 93]
lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

# Execute strict linter commands [cite: 94]
lint-strict:
	flake8 .
	mypy . --strict

# Custom helper rule to compile the wheel and tarball packages [cite: 228, 230]
build:
	python3 setup.py sdist bdist_wheel