"""
Convert CSV data into Moodle enrollment CSV for use on Upload Users page
Be able to specify where the fields we're looking for exist in the CSV.
The main work of this script is creating multiple rows for International
students who need to be placed into multiple groups.
"""

import csv
import re

import click

email_regex: re.Pattern[str] = re.compile(r"@cca\.edu$")
student_types: list[str] = ["First Year", "Transfer", "Graduate"]


def writerows(writer, row, field_map) -> None:
    # sometimes user hasn't created their CCA email yet, if so skip them
    if not (username := re.sub(email_regex, "", row[field_map["email"]].strip())):
        return

    stype = row[field_map["type"]].strip().title()
    if stype not in student_types:
        raise ValueError(f"Unknown student type {stype} for student {username}")

    # look for fields we need and write to output
    writer.writerow(
        {
            "username": username,
            "course1": field_map["course"],
            "group1": stype,
        }
    )
    # if international, write another row with the international group
    intl = row[field_map["intl"]]
    if intl:
        writer.writerow(
            {
                "username": username,
                "course1": field_map["course"],
                "group1": "International",
            }
        )


@click.command()
@click.help_option("-h", "--help")
@click.option("--infile", "-i", help="Input CSV file")
@click.option(
    "--outfile", "-o", default="nso.csv", help="Output CSV file (default: nso.csv)"
)
@click.option(
    "--email", "-e", default="CCA Email", help="Email column (default: CCA Email)"
)
@click.option(
    "--intl",
    default="International?",
    help="International column (default: International?)",
)
@click.option(
    "--type",
    "-t",
    default="Applicant Type",
    help="Student type (First Year, Transfer, Graduate) column (default: Applicant Type)",
)
# TODO option to generate multiple CSVs (one per grad, transfer, first year)
@click.option("--course", "-c", help="Course shortname (e.g. NSO-2024SP)")
def main(**kwargs):
    field_map: dict[str, str] = {
        "email": kwargs["email"],
        "intl": kwargs["intl"],
        "course": kwargs["course"],
        "type": kwargs["type"],
    }
    with open(kwargs["infile"], "r") as csvfile:
        reader = csv.DictReader(csvfile)
        with open(kwargs["outfile"], "w") as outfile:
            writer = csv.DictWriter(
                outfile, fieldnames=["username", "course1", "group1"]
            )
            writer.writeheader()
            for row in reader:
                writerows(writer, row, field_map)


if __name__ == "__main__":
    main()
