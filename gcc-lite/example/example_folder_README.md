# `example` folder overview

Test builds of the cookiecutter template using all default options can be made in this
repository.

In Windows, delete any pre-existing sub-folders in the `example` folder, and run:

```shell
python -m cookiecutter . -o ./gcc-lite/example --no-input
```

Unix and Linux users can alternatively use a `make` command:

```{warning}
Any existing folders will be automatically deleted by executing the `make` command.
```

```shell
make example
```
