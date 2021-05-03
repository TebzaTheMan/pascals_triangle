n = int(input("Enter your n value : "))
rows = [[1]]


def add_1s(row):
    new_row = row.copy()
    new_row.insert(0, 1)
    new_row.append(1)
    return new_row


# calculate pascals triangle numbers
for row_num in range(1, n+1):
    next_row = []
    last_row = rows[row_num-1]

    for index, num in enumerate(last_row, start=0):
        next_num_index = index+1
        if next_num_index < len(last_row):  # checks if next num exists
            next_row.append(num + last_row[next_num_index])
    rows.append(add_1s(next_row))

# print pascals numbers in a triangle format
for row in rows:
    spaced_row = '   '.join(map(str, row))
    num_spaces = int(len(rows)) - int(len(row))
    print(num_spaces*('  ')+spaced_row)
    print('\n')
