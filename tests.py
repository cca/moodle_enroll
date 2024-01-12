import pytest

from .interns import meets_program_criteria, make_enrollment


@pytest.mark.parametrize(
    "input,expected",
    [
        # not an internship program
        (
            {
                "CCA Email": "a@cca.edu",
                "Primary Program of Study Record Status": "In Progress",
                "Primary Program of Study": "Fake Program",
                "Is International Student": "",
                "Latest Class Standing": "Third Year",
            },
            False,
        ),
        # not 'in progress'
        (
            {
                "CCA Email": "a@cca.edu",
                "Primary Program of Study Record Status": "Suspended",
                "Primary Program of Study": "Architecture",
                "Is International Student": "",
                "Latest Class Standing": "Third Year",
            },
            False,
        ),
        # no email
        (
            {
                "CCA Email": None,
                "Primary Program of Study Record Status": "In Progress",
                "Primary Program of Study": "Architecture",
                "Is International Student": "",
                "Latest Class Standing": "Third Year",
            },
            False,
        ),
        # domestic enrollment
        (
            {
                "CCA Email": "a@cca.edu",
                "Primary Program of Study Record Status": "In Progress",
                "Primary Program of Study": "Architecture",
                "Is International Student": "",
                "Latest Class Standing": "Third Year",
            },
            ["a", "ARCHT-INTRN", "Fall 2023", ""],
        ),
        # international enrollment
        (
            {
                "CCA Email": "a@cca.edu",
                "Primary Program of Study Record Status": "In Progress",
                "Primary Program of Study": "Interior Design",
                "Is International Student": "Yes",
                "Latest Class Standing": "Third Year",
            },
            ["a", "INTER-INTRN", "Fall 2023", "International"],
        ),
    ],
)
def test_make_enrollment(input, expected):
    assert make_enrollment(input, "Fall 2023") == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        # not in program
        (
            {
                "CCA Email": "a@cca.edu",
                "Primary Program of Study Record Status": "In Progress",
                "Primary Program of Study": "Architecture",
                "Is International Student": "",
                "Latest Class Standing": "Third Year",
            },
            False,
        ),
        # in program
        (
            {
                "CCA Email": "a@cca.edu",
                "Primary Program of Study Record Status": "In Progress",
                "Primary Program of Study": "Interior Design",
                "Is International Student": "",
                "Latest Class Standing": "Third Year",
            },
            ["a", "INTER-INTRN", "Fall 2023", ""],
        ),
    ],
)
def test_make_enrollment_program_filter(input, expected):
    assert make_enrollment(input, "Fall 2023", "Interior Design") == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        # ARCHT first year, does not meet
        (
            {
                "CCA Email": "a@cca.edu",
                "Primary Program of Study Record Status": "In Progress",
                "Primary Program of Study": "Architecture",
                "Is International Student": "",
                "Latest Class Standing": "First Year",
            },
            False,
        ),
        # ARCHT third year, meets
        (
            {
                "CCA Email": "a@cca.edu",
                "Primary Program of Study Record Status": "In Progress",
                "Primary Program of Study": "Architecture",
                "Is International Student": "",
                "Latest Class Standing": "Third Year",
            },
            True,
        ),
        # ARCHT > 3rd year, also meets
        (
            {
                "CCA Email": "a@cca.edu",
                "Primary Program of Study Record Status": "In Progress",
                "Primary Program of Study": "Architecture",
                "Is International Student": "",
                "Latest Class Standing": "Fourth Year",
            },
            True,
        ),
    ],
)
def test_meets_program_criteria(input, expected):
    assert meets_program_criteria(input) == expected


# test listmode
@pytest.mark.parametrize(
    "input,expected",
    [
        # ARCHT first year, does not meet
        (
            {
                "Student": "fake name",
                "CCA Email": "a@cca.edu",
                "Primary Program of Study Record Status": "In Progress",
                "Primary Program of Study": "Architecture",
                "Is International Student": "",
                "Latest Class Standing": "First Year",
            },
            False,
        ),
        # ARCHT third year, meets
        (
            {
                "Student": "fake name",
                "CCA Email": "a@cca.edu",
                "Primary Program of Study Record Status": "In Progress",
                "Primary Program of Study": "Architecture",
                "Is International Student": "",
                "Latest Class Standing": "Third Year",
            },
            ["fake name", "a@cca.edu"],
        ),
    ],
)
def test_make_enrollment_listmode(input, expected):
    assert make_enrollment(input, "Fall 2023", listmode=True) == expected
