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

## Internship Enrollments Usage

1. Download the "Students for Internship Review" report
1. `pipenv run python report_to_enroll.py -r report.xlsx`
    1. You don't need to pass a `-r` parameter if the report keeps its default name "Students_for_Internship_Review.xlsx"
    1. Generate enrollments for a single program with `-p $PROGRAM` e.g. `-p Architecture`
1. Moodle > [Upload Users](https://moodle.cca.edu/admin/tool/uploaduser/index.php)
    1. Select the CSV
    1. Don't modify user values (e.g. no updates, no default values, etc.)

## NSO Enrollments Usage

This script is used to generate enrollments for the New Student Orientation courses. It lets you specify where in a provided CSV to look for the few pieces of information we need (email, type, international status). Example using CSV of Leave of Absence students: `pipenv run python nso-enroll.py --infile loa.csv -e "Student Institutional Email Address" -t "Program of Study Status" --intl "Student is International" -c "NSO-2024SP"`

```sh
Usage: nso_enroll.py [OPTIONS]

Options:
  -i, --infile TEXT   Input CSV file
  -o, --outfile TEXT  Output CSV file (default: nso.csv)
  -e, --email TEXT    Email column (default: CCA Email)
  --intl TEXT         International column (default: International?)
  -t, --type TEXT     Student type (First Year, Transfer, Grad, Non-Degree,
                      LOA) column
  -c, --course TEXT   Course shortname (e.g. NSO-2024SP)
  --help              Show this message and exit.
```

## LICENSE

[ECL Version 2.0](https://opensource.org/licenses/ECL-2.0)
