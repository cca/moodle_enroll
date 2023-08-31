import argparse

from openpyxl import load_workbook


def row_to_dict(header, row):
    return dict(zip(header, row))


def wd_report_to_enroll_csv(report):
    wb = load_workbook(report)
    sheet = wb.active
    rows = sheet.iter_rows(values_only=True)
    header = next(rows)
    for row in rows:
        row = row_to_dict(header, row)
        print(row)
        exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='report_to_enrol', description='Convert Workday internships report into Moodle enrollment CSV.')
    parser.add_argument('-r', '--report', required=False, default='Students_for_Internship_Review.xlsx')
    args = parser.parse_args()
    wd_report_to_enroll_csv(args.report)
