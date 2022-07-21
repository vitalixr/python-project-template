# Intro

This is a base python project template. It's ready and for python library and
for general project.
Out of the box you get:
* `setup.py` friendly package with command-line entrypoint.
* Testable environment based on `pytest` and `tox`.
* Command-line skeleton based on `click` library.
* Bunch of development libraries for linting `flake8, pep8, ...` and debugging
  `ipython`.


# Quickstart

Prerequisites:
* [pyenv](https://github.com/pyenv/pyenv)
* [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

To create virtualenv and install all base requirements do there `make bootstrap`.
This command creates virtualenv and install all base requirements.
After that you can activate venv and do base test:
```bash
pyenv activate big-bang

# Run test
pytest # or tox
# Run cmd-line interface
big_bang --help
```

# New project

For simplifying I didn't add templating here, so you need rename a couple of
variable and files.
```
cp -r python-project-template new-project
mv big_bang new_project
sed -i 's/big-bang/new-project/g' Makefile
sed -i 's/big-bang/new-project/g' setup.py
sed -i 's/big_bang/new_project/g' setup.py
sed -i 's/big_bang/new_project/g' ./tests/test_main.py

make bootstrap
```
