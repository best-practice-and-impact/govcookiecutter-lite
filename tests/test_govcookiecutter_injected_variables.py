from collections import Counter
from pathlib import Path
from typing import Dict, List, Union

import pytest

# Define the expected counts for each cookiecutter variable - any counts that deviate
# because of other variables are listed at the end of each dictionary
ORGANISATION_HANDLE_COUNT = {
    '"{{ cookiecutter.organisation_handle }}"': 0,
    "`{{ cookiecutter.organisation_handle }}`": 2,
    'u"{{ cookiecutter.organisation_handle }}",': 0,
    '[u"{{ cookiecutter.organisation_handle }}"],': 0,
    '"{{ cookiecutter.organisation_handle }}",': 0,
}
PROJECT_NAME_COUNT = {
    '"{{ cookiecutter.project_name }}"': 0,
    '"{{ cookiecutter.project_name }}",': 0,
    'u"{{ cookiecutter.project_name }}': 0,
    "{{ cookiecutter.project_name }}": 1,
}


def replace_cookiecutter_jinja2_counts(
    count_dictionary: Dict[str, int], jinja2_string: str, replacement_string: str
) -> Dict[str, int]:
    """Create a count of expected Jinja2 variables post-cookiecutter generation.

    After the template is generated, we do not expect any ``jinja2_string``-like text
    to exist, but instead they should be replaced by ``replacement_string``-like text.

    If ``count_dictionary`` contains the key-value pairs of counts of
    ``jinja2_string``-like text pre-cookiecutter generation, then calculate the
    expected counts of ``replacement_string``-like text post-generation. Then set the
    ``jinja2_string`` key (without curly braces and whitespace) to have a value of
    zero - this allows checking that the variable has been safely overwritten.

    Args:
        count_dictionary: A dictionary containing keys that contain ``jinja2_string``,
            and values that are counts of these keys in the original cookiecutter
            template.
        jinja2_string: A string that is present in all the keys of ``count_dictionary``.
        replacement_string: A string that will replace ``jinja2_string`` in the
            outputted cookiecutter project.

    Returns:
        A dictionary containing all the original key-value pairs of
        ``count_dictionary`` but with the ``jinja2_string`` string in each key
        replaced by ``replacement_string``. One extra key of just the ``jinja2_string``
        string without curly braces or whitespaces set to zero.

    """

    # Iterate over `count_dictionary`, replacing the `jinja2_string` contained in its
    # keys with `replacement_string`
    out_dict = {}
    for k, v in count_dictionary.items():
        key_replacement = k.replace(jinja2_string, replacement_string)
        out_dict[key_replacement] = v

    # Get the 2nd element of `jinja2_string`, in other words the
    # "cookiecutter.variable_name" element, and set it to zero. Then return `out_dict`
    out_dict[jinja2_string.split()[1]] = 0
    return out_dict


def recursive_open_and_count_search_terms(
    terms: Union[str, List[str]], folder: Union[str, Path]
) -> Dict[str, int]:
    """Recursively open files in a folder, and count given search terms.

    Args:
        terms: A string of list of strings denoting the search terms.
        folder: A folder containing files to recursively open and count for search
            terms.

    Returns:
        A dictionary where each key-value pair contains each search term, and its
        associated count.

    """

    # Set terms to a list, and get all files in `folder` recursively
    terms = terms if isinstance(terms, List) else [terms]
    all_files = [f for f in Path(folder).rglob("*") if f.is_file()]

    # Initialise a counter, then iterate through the files counting all terms
    word_count = Counter()
    for file in all_files:
        try:
            with open(file, encoding="utf-8") as f:
                word_count.update(Counter(f.read().split()))
                if word_count.get("cookiecutter.using_R"):
                    print(file)
        except UnicodeDecodeError:
            continue
    return {t: word_count.get(t, 0) for t in terms}


# Define the test cases for the `test_injected_counts_correct` test
args_injected_counts_correct = [
    ("organisation_handle", "handle_1", ORGANISATION_HANDLE_COUNT),
    (
        "organisation_handle",
        "handle_2",
        {**ORGANISATION_HANDLE_COUNT, '"{{ cookiecutter.organisation_handle }}",': 0},
    ),
    ("project_name", "Project_1", PROJECT_NAME_COUNT),
    (
        "project_name",
        "Project_2",
        {**PROJECT_NAME_COUNT, "{{ cookiecutter.project_name }}": 1},
    ),
]


@pytest.mark.parametrize(
    "test_input_variable, test_input_value, " "test_input_variable_counts",
    args_injected_counts_correct,
)
def test_injected_counts_correct(
    cookies,
    test_input_variable: str,
    test_input_value: str,
    test_input_variable_counts: Dict[str, int],
) -> None:

    # Generate the expected counts
    test_expected_counts = replace_cookiecutter_jinja2_counts(
        test_input_variable_counts,
        "{{{{ cookiecutter.{variable} }}}}".format(variable=test_input_variable),
        test_input_value,
    )

    # Create a new project adding extra context
    test_output_project = cookies.bake(
        extra_context={
            test_input_variable: test_input_value,
        }
    )

    # Check that the build passes
    assert test_output_project.exit_code == 0
    assert test_output_project.exception is None

    # Check that all instances have been replaced as expected
    test_output_counts = recursive_open_and_count_search_terms(
        list(test_expected_counts.keys()), test_output_project.project_path
    )
    assert test_output_counts == test_expected_counts
