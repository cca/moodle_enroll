"""Get users enrolled in a Moodle course."""

import json
import sys
from pathlib import Path

import click
import requests

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent))
import config

# usage: python core_enrol_get_enrolled_users.py 3606
# 3606 is Eric's staging test course
# https://moodle.cca.edu/webservice/rest/server.php?wstoken=...&wsfunction=core_enrol_get_enrolled_users&moodlewsrestformat=json&courseid=...


def get_enrolled_users(courseid: str):
    """print enrolled users in a course"""
    url: str = config.url
    params: dict[str, str] = {
        "courseid": courseid,
        "moodlewsrestformat": "json",
        "wsfunction": "core_enrol_get_enrolled_users",
        # found at https://moodle.cca.edu/admin/settings.php?section=webservicetokens
        "wstoken": config.token,
    }

    response: requests.Response = requests.get(url, params=params)
    # weirdly this gives not only all the profile and preferences for each user
    # but also all their enrollments in _other_ courses
    data = response.json()

    # pretty print full data
    return data


@click.command(help="Get users enrolled in a Moodle course.")
@click.help_option("-h", "--help")
@click.argument("courseid")
@click.option(
    "--token",
    "-t",
    help="Moodle web service token (overrides .env)",
)
@click.option(
    "--domain",
    "-d",
    help="Moodle domain URL (overrides .env)",
)
def main(courseid, token, domain):
    """Get enrolled users for a course by its numeric ID."""
    if token:
        config.token = token
    if domain:
        config.url = domain + "/webservice/rest/server.php"

    result = get_enrolled_users(courseid)
    click.echo(json.dumps(result, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
