.PHONY: test

help:
	@echo
	@echo "======================================================================"
	@echo
	@echo "🛠  UTILS"
	@echo
	@echo "repl:       open REPL w/ bpython"
	@echo
	@echo "📊 CODE QUALITY"
	@echo
	@echo "test:       run unit tests, view basic coverage report in terminal"
	@echo "cov:        view HTML coverage report in browser"
	@echo "lint:       lint using flake8"
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
# 🛠 UTILS
#

repl:
	poetry run bpython

#
# 📊 CODE QUALITY
#

test:
	poetry run coverage run --source='src' -m pytest -v && poetry run coverage report -m

cov:
	poetry run coverage html; open htmlcov/index.html

lint:
	poetry run flake8 src test

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
