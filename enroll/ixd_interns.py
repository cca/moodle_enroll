# this expects a CSV with an email and international status column
# then exports the IXD intern enrollment CSV
# usage: python enroll/ixd_interns.py "Fall 2025" data/ixd.csv > enrollments.csv
import csv
import sys

COURSE: str = "IXDSN-INTRN"
EMAIL_COLUMN: str = "email"
INTL_COLUMN: str = "international"


def make_rows(row: dict[str, str], semester: str) -> list[list[str]]:
    username: str = row[EMAIL_COLUMN].strip().replace("@cca.edu", "")
    rows: list[list[str]] = [[username, COURSE, semester]]
    if row[INTL_COLUMN].strip().lower() == "yes":
        rows.append([username, COURSE, "International"])
    return rows


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: python enroll/ixd_interns.py "Fall 2025" data/ixd.csv')
        print('data/ixd.csv should have "email" and "international" columns')
        exit(1)

    semester: str = sys.argv[1]
    with open(sys.argv[2], "r") as fh:
        reader = csv.DictReader(fh)
        with open("enrollments.csv", "w") as outfile:
            writer = csv.writer(outfile)
            # header
            writer.writerow(["username", "course1", "group1"])
            for row in reader:
                enrollments = make_rows(row, semester)
                for e in enrollments:
                    writer.writerow(e)

    print(
        "Created enrollments.csv. Upload Users: https://moodle.cca.edu/admin/tool/uploaduser/"
    )
