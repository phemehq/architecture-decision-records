SPHINXOPTS    ?=
SPHINXBUILD   ?= $(VENV)/bin/sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
VENV          = ../.venv
PIP           = $(VENV)/bin/pip
PYTHON        = $(VENV)/bin/python

.PHONY: help install build run livehtml clean Makefile

help:
	@echo "Usage:"
	@echo "  make install   Create .venv and install dependencies"
	@echo "  make build     Build HTML documentation"
	@echo "  make run       Serve built docs on http://localhost:8000"
	@echo "  make livehtml  Live-reload server (rebuilds on file change)"
	@echo "  make clean     Remove build output"

install:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip -q
	$(PIP) install -r requirements.txt
	@echo "Done. Run 'make build' next."

build:
	$(SPHINXBUILD) -b html -W --keep-going "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)
	@echo "Build complete: $(BUILDDIR)/html/index.html"

run:
	@echo "Serving docs at http://localhost:8000"
	$(PYTHON) -m http.server 8000 --directory "$(BUILDDIR)/html"

livehtml:
	$(VENV)/bin/sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)

clean:
	rm -rf "$(BUILDDIR)"
	@echo "Cleaned."

%: Makefile
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
