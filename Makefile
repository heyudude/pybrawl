# Define required macros here
SHELL = /bin/sh

SRCDIR = ./pyroyale
TESTDIR = ./tests

clean:
	python3 setup.py clean
	rm -rf build dist .pytest_cache *.egg-info $(SRCDIR)/__pycache__ $(TESTDIR)/__pycache__ MANIFEST

install:
	python3 setup.py install

develop:
	python3 setup.py develop

test:
	python3 setup.py test

coverage:
	coverage run setup.py test
	coverage xml

sonar: coverage
	sonar-scanner -Dsonar.projectVersion=`python -c "import sys; from pyroyale import __version__; sys.stdout.write(__version__)"`

upload:
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
