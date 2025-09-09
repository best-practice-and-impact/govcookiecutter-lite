# Modifying govcookiecutter-lite

!!! warning

    It's strongly recommended you build an example project to test that your changes work!


Govcookiecutter-lite uses the [`cookiecutter` Python package][cookiecutter] to build
template project structures. In turn, [`cookiecutter` uses Jinja templating to inject
user-defined variables][jinja] into files, file names, and folder names. Most of these
variables are based on answers to prompts when you run the `cookiecutter` command.

## `cookiecutter` template generation

When you open your terminal and run:

```shell
cookiecutter https://github.com/best-practice-and-impact/govcookiecutter-lite.git
```

you'll see a list of prompts to answer; one of them is `project_name`.

Your answer for `project_name` is used to overwrite every instance of
`{{ cookiecutter.project_slug }}`. The first instance is the `govcookiecutter-lite` folder
`{{ cookiecutter.project_slug }}`, which becomes your outputted project!

This means every folder and file contained within the `{{ cookiecutter.project_slug }}`
folder becomes part of your output project, including their content. Anything else
outside of this folder in `govcookiecutter-lite` will not exist in the outputted project.

### Understanding `cookiecutter.json`

The prompts, and their default responses are defined in `cookiecutter.json`. Here, any
keys starting with `_` are not shown to the user, but provide template extensions.

One such extension is `jinja2_time.TimeExtension`, which is used to add the correct
year in the `{{ cookiecutter.project_slug }}/LICENSE` file.

All other keys are used to inject the user responses throughout the template. This
happens wherever you see `{{ cookiecutter.{KEY} }}`, where `{KEY}` is the key in
question.

The values in `cookiecutter.json` are the default responses, shown in squared brackets
to the user. If the user does not enter a response, these default values are used.
Values that are lists are shown as numerical options to the user, with the first list
element as the default value.

Note that these default values can also contain Jinja templating!

## Validating user entries

User entries are validated with pre-generation hooks, which are defined in
`hooks/pre_gen_project.py`. These hooks run before a project is created and, if they
fail, will not create the project.

Currently we only raise a warning if the user includes underscores in the project name.
It is recommend to only include underscores in package names if they improve readability.

## Tests, coverage, and continuous integration

All pre- and post-generation hooks should be fully tested, alongside any generic
functions that we want to supply to users within the `{{ cookiecutter.project_slug }}`
package. These tests should be written in `tests` or
`{{ cookiecutter.project_slug }}/tests` as appropriate.

Coverage also only covers the `hooks` and `{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}` folders.

### Testing Jinja templating

Most of the tests are straightforward, and comprehensive. However, to test the Jinja
injection of user responses, the `test_govcookiecutter_injected_variables.py` script
adopts a test-driven development approach to completeness.

This test parses all the content of the `{{ cookiecutter.project_slug }}` folder, and
counts the number of times the replacement variable and its variations appear.

The constant dictionary variables at the top of the test script define the different
variations of Jinja templating expected for each prompt, and their expected counts.
The dictionary keys are replaced during the test with the test input variables.

If you modify the content, beware that these counts may change, so you will have to
change these counts to pass the tests.

### Continuous integration

Continuous integration (CI) is provided by GitHub Actions. For all pushes to the
repository, GitHub Actions will:

- install the requirements
- run pre-commit hooks on all files
- create the documentation to check for errors and warnings
  - only errors are checked for Windows
- check for broken external links in the documentation
- run tests and coverage
- upload coverage reports to CodeCov

These "on push" CI checks are run on Ubuntu, macOS, and Windows operating systems, as
well as Python 3.6+. This Action can be found at `workflows/govcookiecutter-build.yml`.

When a pull request is raised, GitHub Actions will also:

- build an example project
- navigate into the example project
- initialise Git
- install requirements

These "on pull request" CI checks are run on Ubuntu, and macOS operating systems, as
well as Python 3.9+.

## Releases

Pull requests are raised on GitHub, and approved features are merged into `main`. [We
then use semantic versioning to number our releases][semver]. This helps our users
select a different version of `govcookiecutter-lite` to use based on their individual needs.

[cookiecutter]: https://cookiecutter.readthedocs.io
[github-issues]: https://github.com/best-practice-and-impact/govcookiecutter/issues
[html5-email-format]: https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address
[jinja]: https://jinja.palletsprojects.com
[semver]: https://semver.org/
