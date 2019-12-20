# overview

Algorithms and data structures from:

* Grokking Algorithms
* Hacker Rank

because:

* curiosity
* [tech industry hiring practices are folkloric and irrational](https://www.zachvalenta.com/blog/hiring-in-tech.html)

# run locally

* dependencies - [make virtual environment and activate](https://github.com/zachvalenta/dotfiles/blob/master/.bash_profile#L80)
* dependencies - `make install`
* env var - `ln -sf .env.dev .env`
* everything else - `make help`

```sh
======================================================================

🛠  UTILS

repl:       open REPL w/ bpython

📊 CODE QUALITY

test:       run unit tests, view basic coverage report in terminal
cov:        view HTML coverage report in browser
lint:       lint using flake8
fmt:        autoformat using black

📦 DEPENDENCIES

deps:       dependency graph
install:    install dependencies from requirements.txt
purge:      remove any installed pkg *not* in requirements.txt
freeze:     freeze dependencies into requirements.txt

======================================================================
```
