# overview

Algorithms and data structures from:

* [Grokking Algorithms](https://www.manning.com/books/grokking-algorithms)
* [Hacker Rank](https://www.hackerrank.com/interview/interview-preparation-kit)

including implementations of:

* __search__: binary, breadth-first, Dijkstra
* __sort__: quick, selection

because:

* curiosity
* [tech industry hiring practices are folkloric and irrational](https://www.zachvalenta.com/blog/hiring-in-tech.html)

# run locally

* install dependencies - `poetry install`
* install Git hooks - `make hooks`
* everything else - `make help`

```makefile
======================================================================

🐛  DEBUG

pdb:        run unit tests w/ pdb breakpoint
repl:       open REPL w/ bpython

📊 CODE QUALITY

test:       run unit tests, view basic coverage report in terminal
cov:        view HTML coverage report in browser
lint:       lint using flake8
fmt:        autoformat using black
hooks:      set Git hooks w/ pre-commit

📦 DEPENDENCIES

env:        show environment info
deps:       list prod dependencies

======================================================================
```
