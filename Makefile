.PHONY: test

help:
	@echo
	@echo "======================================================================"
	@echo
	@echo "📊 CODE QUALITY"
	@echo
	@echo "repl:       open REPL w/ bpython"
	@echo "test:       run unit tests, view basic coverage report in terminal"
	@echo "cov:        view HTML coverage report in browser"
	@echo "lint:       lint"
	@echo "lint-fix:   fix lint err"
	@echo "fmt:        autoformat using black"
	@echo "hooks:      set Git hooks w/ pre-commit"
	@echo
	@echo "📦 DEPENDENCIES"
	@echo
	@echo "env:        show environment info"
	@echo "deps:       list prod dependencies"
	@echo
	@echo "======================================================================"
	@echo

#
# 📊 CODE QUALITY
#

repl:
	export PYTHONSTARTUP='./repl.py' && poetry run bpython

test:
	poetry run coverage run --source='src' -m pytest -sv --pdb && poetry run coverage report -m

cov:
	poetry run coverage html; open htmlcov/index.html

lint:
	poetry run ruff check

lint-fox:
	poetry run ruff check --fix

fmt:
	poetry run black src test

hooks:
	poetry run pre-commit install -t pre-commit; poetry run pre-commit install -t pre-push

#
# 📦 DEPENDENCIES
#

env:
	poetry env info

deps:
	poetry show --tree --no-dev
