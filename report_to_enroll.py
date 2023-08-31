import argparse
import csv
import re
import warnings

from openpyxl import load_workbook


program_to_course_map = {
    'Architecture': 'ARCHT-INTRN',
    'Graduate Architecture': 'MARCH-INTRN',
    'Graphic Design': 'GRAPH-INTRN',
    'Industrial Design': 'INDUS-INTRN',
    'Interaction Design': 'IXDSN-INTRN',
    'Interior Design': 'INTER-INTRN',
}
programs_with_internship = list(program_to_course_map.keys())


def row_to_dict(header, row):
    return dict(zip(header, row))


def make_enrollment(student):
    # students must be actively enrolled in a program with a required internship
    if student['Primary Program of Study'] in programs_with_internship and student['Primary Program of Study Record Status'] == 'In Progress' and student['CCA Email']:
        username = re.sub('@cca.edu', '', student['CCA Email'])
        course = program_to_course_map[student['Primary Program of Study']]
        group = 'International' if student['Is International Student'] == 'Yes' else ''
        return [username, course, group]
    return False


def wd_report_to_enroll_csv(report):
    # silence "Workbook contains no default style" warning
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        wb = load_workbook(report)
    sheet = wb.active
    rows = sheet.iter_rows(values_only=True)
    header = next(rows)
    with open('enrollments.csv', 'w') as file:
        writer = csv.writer(file)
        # write CSV header row
        writer.writerow(['username', 'course1', 'group1'])
        for row in rows:
            student = row_to_dict(header, row)
            e = make_enrollment(student)
            if e: writer.writerow(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='report_to_enrol', description='Convert Workday internships report into Moodle enrollment CSV.')
    parser.add_argument('-r', '--report', required=False, default='Students_for_Internship_Review.xlsx')
    args = parser.parse_args()
    wd_report_to_enroll_csv(args.report)
