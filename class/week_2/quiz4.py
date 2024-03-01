def quiz4():
    int_row = int(input("Number of rows: "))
    int_column = int(input("Number of rows: "))
    int_grid = int(input("Grid size: "))
    row_unit = ""
    column_unit = ""
    for i in range(int_column):
        row_unit += "+" + "-" * int_grid
    row_unit += '+'
    for i in range(int_column):
        column_unit += "|" + " " * int_grid
    column_unit += "|"
    for i in range(int_row):
        print(row_unit)
        print(column_unit)
    print(row_unit)


# not the best method
