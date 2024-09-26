from boriy_core import XLSXSheet


if __name__ == "__main__":
    sheet = XLSXSheet("A", 1)

    print("Sheet", sheet)

    sheet.write_cell(100, 100, "Жопа")

    print("Sheet", sheet)

    cell = sheet.find_cell_by_coordinate(100, 100)

    print("Cell 100x100", cell.value if cell else cell)
