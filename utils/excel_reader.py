from openpyxl import load_workbook


class ExcelReader:

    def __init__(self, file_path):
        self.workbook = load_workbook(file_path)

    def get_data(self, sheet_name):

        sheet = self.workbook[sheet_name]

        rows = list(sheet.rows)

        headers = [cell.value for cell in rows[0]]

        data = []

        for row in rows[1:]:

            record = {}

            for header, cell in zip(headers, row):
                record[header] = cell.value

            data.append(record)

        return data