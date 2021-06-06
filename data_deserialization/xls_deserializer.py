import xlrd
import os
import pprint

# xls or xlsx
DATADIR = "../assets/"
DATAFILE = "MOCK_DATA.xlsx"
SHEET_NUMBER = 0
ROW = 2
COLUMN = 3


def parse_excel(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(SHEET_NUMBER)
    data = [[sheet.cell_value(r, col)
             for col in range(sheet.ncols)]
            for r in range(sheet.nrows)]
    print("\n List Comprehension")
    print("data[{}][{}]:{}".format(ROW, COLUMN, data[ROW][COLUMN]))

    print("\n Cells in a nested loop:")
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            print(sheet.cell_value(row, col))

    # EXTRA
    print("\n ROW , COLUMNS and CELLS")
    print('Number of rows in the sheet {}: {} \n'.format(SHEET_NUMBER, sheet.nrows))
    print("Type of data in cell (row {}, col {}): {} \n".format(ROW, COLUMN, sheet.cell_type(ROW, COLUMN)))
    print("Value in cell (row {}, col {}): {} \n".format(ROW, COLUMN, sheet.cell_value(ROW, COLUMN)))
    print("get slice of values in column {} from row 1 -> 3: {} \n".format(COLUMN,
                                                                           sheet.col_values(COLUMN, start_rowx=1,
                                                                                            end_rowx=4)))
    # convert from excel time to python datetime
    # print xlrd.xldate_as_typle(exceltime, 0)


if __name__ == "__main__":
    datafile = os.path.join(DATADIR, DATAFILE)
    parse_excel(datafile)
