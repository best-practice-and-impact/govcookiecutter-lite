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

## Quickstart Guide

``` shell title="getting started"
pip install cookiecutter
python -m cookiecutter https://github.com/best-practice-and-impact/govcookiecutter-lite.git
```

[aqua-book]: https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government
[blog-post]: https://dataingovernment.blog.gov.uk/2021/07/20/govcookiecutter-a-template-for-data-science-projects/
[cruft]: https://github.com/cruft/cruft
[docs-pre-commit]: ./CONTRIBUTING.md#getting-started
[drivendata]: http://drivendata.github.io/cookiecutter-data-science/
[govcookiecutter]: https://github.com/best-practice-and-impact/govcookiecutter.git
[homebrew]: https://brew.sh/
[issue-windows-os]: https://github.com/best-practice-and-impact/govcookiecutter/issues/20
[pluralsight]: https://www.pluralsight.com/tech-blog/managing-python-environments/
[youtube]: https://www.youtube.com/watch?v=N7_d3k3uQ_M