import pytest

from .report_to_enroll import meets_program_criteria, make_enrollment

@pytest.mark.parametrize('input,expected', [
    # not an internship program
    ({'CCA Email': 'a@cca.edu', 'Primary Program of Study Record Status': 'In Progress', 'Primary Program of Study': 'Fake Program', 'Is International Student': ''}, False),
    # not 'in progress'
    ({'CCA Email': 'a@cca.edu', 'Primary Program of Study Record Status': 'Suspended', 'Primary Program of Study': 'Architecture', 'Is International Student': ''}, False),
    # no email
    ({'CCA Email': None, 'Primary Program of Study Record Status': 'In Progress', 'Primary Program of Study': 'Architecture', 'Is International Student': ''}, False),
    # domestic enrollment
    ({'CCA Email': 'a@cca.edu', 'Primary Program of Study Record Status': 'In Progress', 'Primary Program of Study': 'Architecture', 'Is International Student': ''}, ['a','ARCHT-INTRN','']),
    # international enrollment
    ({'CCA Email': 'a@cca.edu', 'Primary Program of Study Record Status': 'In Progress', 'Primary Program of Study': 'Interior Design', 'Is International Student': 'Yes'}, ['a','INTER-INTRN','International']),
])
def test_make_enrollment(input, expected):
    assert make_enrollment(input) == expected


@pytest.mark.parametrize('input,expected', [
    # not in program
    ({'CCA Email': 'a@cca.edu', 'Primary Program of Study Record Status': 'In Progress', 'Primary Program of Study': 'Architecture', 'Is International Student': ''}, False),
    # in program
    ({'CCA Email': 'a@cca.edu', 'Primary Program of Study Record Status': 'In Progress', 'Primary Program of Study': 'Interior Design', 'Is International Student': ''}, ['a','INTER-INTRN','']),
])
def test_make_enrollment_program_filter(input, expected):
    assert make_enrollment(input, 'Interior Design') == expected
