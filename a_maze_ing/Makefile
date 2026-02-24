.PHONY: install run debug clean lint lint-strict build
install:
	python3 -m pip install flake8 mypy wheel setuptools
run:
	python3 a_maze_ing.py config.txt
debug:
	python3 -m pdb a_maze_ing.py config.txt
clean:
	rm -rf __pycache__ .mypy_cache build dist mazegen.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -f *.whl *.tar.gz
lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
lint-strict:
	flake8 .
	mypy . --strict
build:
	python3 setup.py sdist bdist_wheel
	mv dist/* .
	rm -rf build dist mazegen.egg-info