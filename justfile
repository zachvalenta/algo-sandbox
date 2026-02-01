# 📊 CODE QUALITY

# open REPL w/ bpython
repl:
    export PYTHONSTARTUP='./repl.py' && poetry run bpython -q

# run unit tests, view basic coverage report in terminal
test:
    poetry run coverage run --source='src' -m pytest -sv --pdb && poetry run coverage report -m

# view HTML coverage report in browser
cov:
    poetry run coverage html
    open htmlcov/index.html

# lint code
lint:
    poetry run ruff check

# fix lint errors
lint-fix:
    poetry run ruff check --fix

# autoformat using black
fmt:
    poetry run black src test

# set Git hooks w/ pre-commit
hooks:
    poetry run pre-commit install -t pre-commit
    poetry run pre-commit install -t pre-push

# 📦 DEPENDENCIES

# show environment info
env:
    poetry env info

# list prod dependencies
deps:
    poetry show --tree --no-dev
