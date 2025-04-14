# Ad Hoc Enrollments Scripts

Convert reports into Moodle enrollments CSVs.

## Setup

Prerequisites:

- Access to "Students for Internship Review" report in Workday (ask AIS)
- Python 3
- uv (`brew install uv`)

```sh
uv install
uv run pytest -k enroll # run tests
```

## Multiple Groups

In a Moodle enrollment CSV, we can add someone to multiple courses using `course1`, `course2`, etc. columns. However, this means a row with a single `course1` but multiple groups (`group1`, `group2`) doesn't add the user to multiple groups in the course (`group2` would be a group in `course2`). To add a student to multiple groups in the same course, create multiple rows with different groups:

| username | course1 | group1 |
|----------|---------|--------|
| maria | ART-101 | transfer |
| maria | ART-101 | international |

This is how interns.py adds students to multiple groups in the same course.

## Internship Enrollments Usage

Generate enrollments CSV for Moodle from Workday report.

1. Download the "Students for Internship Review" report
1. `uv run python enroll/interns.py -r report.xlsx -s "Fall 2024"`
    1. You don't need to pass a `-r` parameter if the report keeps its default name "Students_for_Internship_Review.xlsx"
    1. `-s` is the semester group for students
    1. Generate enrollments for a single program with `-p $PROGRAM` e.g. `-p Architecture`
1. Go to Moodle > [Upload Users](https://moodle.cca.edu/admin/tool/uploaduser/index.php)
    1. Select the CSV
    1. Don't modify user values (e.g. no updates, no default values, etc.)

## NSO Enrollments Usage

This script is used to generate enrollments for the New Student Orientation courses. It lets you specify where in a provided CSV to look for the few pieces of information we need (email, type, international status). Example using CSV of Leave of Absence students: `uv run python enroll/nso.py --infile loa.csv -e "Student Institutional Email Address" -t "Program of Study Status" --intl "Student is International" -c "NSO-2024SP"`

```sh
Usage: nso.py [OPTIONS]

Options:
  -h, --help          Show this message and exit.
  -i, --infile TEXT   Input CSV file
  -o, --outfile TEXT  Output CSV file (default: nso.csv)
  -e, --email TEXT    Email column (default: CCA Email)
  --intl TEXT         International column (default: International?)
  -t, --type TEXT     Student type (First Year, Transfer, Graduate) column
                      (default: Applicant Type)
  -c, --course TEXT   Course shortname (e.g. NSO-2024SP). If {type} is present
                      in the course name, it will be replaced with the student
                      type (GRAD, TRSFR, FRESH).
```

## LICENSE

[ECL Version 2.0](https://opensource.org/licenses/ECL-2.0)
