# Define required macros here
SHELL = /bin/sh

SRCDIR = ./pybrawl
TESTDIR = ./tests

clean:
	python3 setup.py clean
	rm -rf build dist .pytest_cache *.egg-info $(SRCDIR)/__pycache__ $(TESTDIR)/__pycache__ MANIFEST .scannerwork .openapi-generator/ htmlcov/ .coverage coverage.xml

delete-models:
	rm -rf docs
	rm -rf test
	rm -rf pybrawl

install:
	pip3 install -r requirements.txt
	python3 setup.py install

develop:
	pip3 install -r requirements.txt
	python3 setup.py develop

test-depend:
	pip3 install -r test-requirements.txt
	pip3 install coverage pytest pytest-runner requests_mock

test: test-depend
	python3 setup.py test

integration: develop
	python3 -m pytest -rApP integration

coverage: test-depend
	coverage run setup.py test
	coverage xml

coverage-html: coverage
	coverage html

sonar: coverage
	sonar-scanner -Dsonar.projectVersion=`python -c "import sys; from pybrawl._version import __version__; sys.stdout.write(__version__)"`

upload:
	python3 setup.py sdist bdist_wheel
	twine upload dist/*

swagger: delete-models
	openapi-generator generate -i https://raw.githubusercontent.com/heyudude/brawlstars-swagger/master/bs_swagger.yaml -g python -DpackageName=pybrawl -o .
	cat templates/README_suffix.md >> README.md

swagger-local: delete-models
	java -jar bin/openapi-generator-cli-4.3.1.jar generate -i ../brawlstars-swagger/bs_swagger.yaml -g python --config ../brawlstars-swagger/bs_config.yaml
	cat templates/README_suffix.md >> README.md

swagger-latest: delete-models
	java -jar ../openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar generate -g python -i ../brawlstars-swagger/bs_swagger.yaml --config ../brawlstars-swagger/bs_config.yaml 
	cat templates/README_suffix.md >> README.md
