.DEFAULT_GOAL := help
DIRECTORIES = $$(find -wholename ./src -o -wholename ./incolume* -o -wholename ./tests)
PKGNAME := "incolume"
PYTHON_VERSION := 3.10

.PHONY: clean
clean:   ## Shallow clean into environment (.pyc, .cache, .egg, .log, et all)
	@echo -n "Starting cleanning environment .."
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*.log' -exec rm -f {} \;
	@find ./ -name '*.log.*' -exec rm -f {} \;
	@find ./ -name ".cache" -exec rm -fr {} \;
	@find ./ -name "*.egg-info" -exec rm -rf {} \;
	@find ./ -name "*.coverage" -exec rm -rf {} \;
	@find ./ -maxdepth 1 -type d -name "*cov*" -exec rm -rf {} \;
	@rm -fv cov.xml poetry.toml
	@rm -rf docs/_build
	@echo " finished!"

.PHONY: clean-all
clean-all: clean   ## Deep cleanning into environment (dist, build, htmlcov, .tox, *_cache, et all)
	@echo "Starting Deep cleanning .."
	@rm -rf dist
	@rm -rf build
	@rm -rf htmlcov
	@rm -rf coverage_report
	@rm -rf .tox
	@find ./ \( -name "*_cache" -o -name '*cache__' \) -exec rm -rf {} 2> /dev/null \;
	@#fuser -k 8000/tcp &> /dev/null
	@#poetry env list|awk '{print $$1}'|while read a; do poetry env remove $${a} 2> /dev/null && echo "$${a} removed."|| echo "$${a} not removed."; done
	@echo "Deep cleaning finished!"

.PHONY: check-black
check-black: ## black checking
	@echo "Black checking .."
	@poetry run black --check $(DIRECTORIES)

.PHONY: check-flake8
check-flake8: ## flake8 checking
	@echo "flake8 checking .."
	@poetry run flake8 --config pyproject.toml $(DIRECTORIES)

.PHONY: check-pylama
check-pylama: ## pylama checking
	@echo "pylama checking .."
	@poetry run pylama $(DIRECTORIES)

.PHONY: check-isort
check-isort:  ## check isort
	@echo "isort checking .."
	@poetry run isort --check --atomic --py all $(DIRECTORIES)

.PHONY: check-mypy
check-mypy: ## mypy checking
	@echo "mypy checking .."
	@poetry run mypy $(DIRECTORIES)

.PHONY: check-pylint
check-pylint: ## pylint checking
	@echo "pylint checking .."
	@poetry run pylint $(DIRECTORIES)

.PHONY: check-pydocstyle
check-pydocstyle: ## docstring checking
	@echo "pydocstyle checking .."
	@poetry run pydocstyle $(DIRECTORIES)

.PHONY: changelog
changelog:   ## Update changelog file
	@poetry run python -c "from incolumepy.utils.changelog import update_changelog; \
	update_changelog(changelog_file='CHANGELOG.md')"
	@echo 'Atualização de CHANGELOG realizada com sucesso.'

.PHONY: help
help:  ## Show this instructions
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)


.PHONY: publish-testing
publish-testing: ## Publish on test.pypi.org
	@poetry publish -r testpypi --build


.PHONY: retrocompatibility
retrocompatibility: ## Run tox and check retrompatibility betwen python versions
	@poetry run tox -e py36,py37,py38,py39,py310,py311


.PHOMY: setup
setup: ## setup environment python with poetry end install all dependences
	@poetry env use $(PYTHON_VERSION)
	@git config core.hooksPath .git-hooks
	@poetry install
