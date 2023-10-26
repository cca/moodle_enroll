# Internship Course Enrollments

Convert Workday report into Moodle enrollments CSV.

## Setup

Prerequisites:

- Access to "Students for Internship Review" report in Workday (ask AIS)
- Python 3
- Pipenv (`brew install pipenv`)

```sh
pipenv install
pipenv run test # run tests
```

## Usage

1. Download the "Students for Internship Review" report
1. `pipenv run python report_to_enroll.py -r report.xlsx`
    1. You don't need to pass a `-r` parameter if the report keeps its default name "Students_for_Internship_Review.xlsx"
    1. Generate enrollments for a single program with `-p $PROGRAM` e.g. `-p Architecture`
1. Moodle > [Upload Users](https://moodle.cca.edu/admin/tool/uploaduser/index.php)
    1. Select the CSV
    1. Don't modify user values (e.g. no updates, no default values, etc.)

## LICENSE

[ECL Version 2.0](https://opensource.org/licenses/ECL-2.0)
