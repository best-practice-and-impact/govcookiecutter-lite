import string
import sys
import warnings


def check_repo_name_structure(repo_name: str) -> None:
    """Check if the repo name follows the correct structure.

    Args:
        repo_name: The name of the repo to check.

    Raises:
        ValueError: If the repo name does not follow the correct structure.
    """
    if len(repo_name) > 88:
        raise ValueError(
            "Repo name must not exceed 88 characters."
        )

    allowed_characters = string.ascii_lowercase + string.digits + "_"
    if any(char not in allowed_characters for char in repo_name):
        raise ValueError(
            "Repo name contains invalid characters. Only lowercase letters, "
            "digits, and underscores are allowed."
        )

    if "_" in repo_name:
        if repo_name.startswith("_"):
            raise ValueError(
                "Repo name must not start with an underscore."
            )
        elif repo_name.endswith("_"):
            raise ValueError(
                "Repo name must not end with an underscore."
            )
        else:
            warnings.warn(
                "Underscores are discouraged in Python package ",
                "names unless they improve readability.",
                UserWarning
            )

if __name__ == "__main__":

    {{ cookiecutter.update({
        "project_slug": cookiecutter.project_name.lower()
        |replace(' ', '_')
        |replace('-', '_')
        |replace('.', '_')
        |trim()
        })
    }}

    # Check the format of the contact email address supplied is a valid one
    check_repo_name_structure("{{ cookiecutter.project_slug }}")

    sys.exit(0)
