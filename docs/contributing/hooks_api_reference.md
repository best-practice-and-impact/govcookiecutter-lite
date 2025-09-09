## hooks folder overview

This folder contains any pre- and post-generation hooks used by the `cookiecutter`
Python package. These are used to customise the created repository based on the
user's requirements, and perform automated tasks such as removing folders.

Full documentation on pre- and post-generation hooks is available in
the [`cookiecutter` documentation][cookiecutter-hooks].

## `hooks` API reference

This page gives an overview of all public `hooks` objects, functions and methods. All
classes and functions exposed in `hooks.*` namespace are public.

## Cookiecutter pre-generation hooks

These are functions run after user input, but before project generation. If any
pre-generation hooks fail, the project will not be generated.

::: hooks.pre_gen_project

## Cookiecutter post-generation hooks

These are functions run after initial project generation by the `cookiecutter`
package. These include moving the selected organisational frameworks to the correct
location, as well as deleting unnecessary files and folders. If any post-generation
hooks fail, the generated project will be rolled-back, and deleted.


### Post-generation clean up

::: hooks.post_gen_project

[cookiecutter-hooks]: https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html
