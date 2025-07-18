# `docs` folder overview

This folder contains documentation for `govcookiecutter-lite`. These are written in MyST Markdown files with Sphinx compatibility.

```{warning}
Further details to consider when modifying these files are supplied in the [contributing guidance][contributing-guidance].
```

To include documentation from the `{{ cookiecutter.project_slug }}`
folder without duplicating it, refer to it in a file within the `docs/{{ cookiecutter.project_slug }}` folder.

To build the documentation, run:

```shell
sphinx-build -b html ./docs ./docs/_build
```

Unix and Linux users can alternatively run the `docs` command from [`Makefile`][docs-makefile] using
the `make` utility at the top-level of this repository.

```shell
make docs
```

The HTML-version of this documentation can then be viewed at `docs/_build/index.html`,
relative to the top-level of this repository.

