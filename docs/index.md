## What is govcookiecutter-lite?

A lightweight cookiecutter template for analytical Python-based projects within
His Majesty's Government, and wider public sector.

## Project structure layout

The cookiecutter template generated for each project will follow this folder structure:

```shell
your_project/
├── docs/
│   └── ...
├── your_project/
│   ├── example_module/
│   │   └── ...
│   └── ...
├── tests/
│   └── ...
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── pyproject.toml
└── README.md
```

More information on these top level files can be found in [created folder structure section][created-folder-structure]

## Quickstart Guide

Govcookiecutter-lite only has one package requirement; `cookiecutter`. The following two lines can be pasted and run in a python virtual environment and will install cookiecutter, then use the govcookiecutter-lite template to create your new project.


``` shell
pip install cookiecutter
python -m cookiecutter https://github.com/best-practice-and-impact/govcookiecutter-lite.git
```
Further details on the prompts asked and what they mean can be found in [creation prompts][prompts].

## Picking between Govcookiecutter and Govcookiecutter-lite

We have tabulated the differences between the versions to help selecting which version best suites your use case.
Note it is possible to add items such as pre-commit hooks and buildable documentation post creation, this table simply denotes what is included at project creation. 

| Feature                          | [Govcookiecutter][govcookiecutter] | [Govcookiecutter-lite][govcookiecutter-lite] |
|-----------------------------------|:-----------------:|:---------------------:|
| Python Project Template           | ✓                 | ✓                     |
| Documentation Folder with Analytical QA | ✓           | ✓                     |
| Unit test folder                        | ✓           | ✓                     |
| Simplified setup prompts                | ✗           | ✓                     |
| Example code and unit tests             | ✓           | ✗                     |
| HTML Buildable Documentation            | ✓           | ✗                     |
| Pre-commit hooks                       | ✓           | ✗                     |
| Options to include R                    | ✓           | ✗                     |
| Options to specify if development is in locked down environment | ✓ | N/A *|
|Platform specific issue and pull request templates| ✓ |  ✗| 

\* This option is not included in govcookiecutter-lite as it relates to pre-commit hooks



[prompts]: created_project_structure/prompts.md
[created-folder-structure]: created_project_structure/created_folder_structure.md
[aqua-book]: https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government
[blog-post]: https://dataingovernment.blog.gov.uk/2021/07/20/govcookiecutter-a-template-for-data-science-projects/
[cruft]: https://github.com/cruft/cruft
[docs-pre-commit]: contributing/CONTRIBUTING.md#getting-started
[drivendata]: http://drivendata.github.io/cookiecutter-data-science/
[govcookiecutter]: https://github.com/best-practice-and-impact/govcookiecutter.git
[homebrew]: https://brew.sh/
[issue-windows-os]: https://github.com/best-practice-and-impact/govcookiecutter/issues/20
[pluralsight]: https://www.pluralsight.com/tech-blog/managing-python-environments/
[youtube]: https://www.youtube.com/watch?v=N7_d3k3uQ_M
[govcookiecutter]: https://github.com/best-practice-and-impact/govcookiecutter/tree/main
[govcookiecutter-lite]: https://github.com/best-practice-and-impact/govcookiecutter-lite/tree/main
