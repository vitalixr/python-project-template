.PHONY: bootstrap

project_name=big-bang
python_version=3.10.4
pip="$(shell pyenv root)/versions/$(project_name)/bin/pip"


bootstrap:
ifeq ($(shell pyenv virtualenvs | grep -q $(project_name); echo $$?), 1)
	pyenv virtualenv $(python_version) $(project_name)
endif
	$(pip) install -r requirements-dev.txt
	$(pip) install -U pip
	$(pip) install -e .
