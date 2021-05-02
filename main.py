'''
print the pascals triangle based on the row number given by user
e.g 2
        1
    1       1
1       2       1

Goal 1 : get the numbers
goal 2 : print the numbers in a triangle format

'''
n = int(input("Enter your n value : "))
rows = [[1]]


def add_1s(row):
    new_row = row.copy()
    new_row.insert(0, 1)
    new_row.append(1)
    return new_row


for row_num in range(1, n+1):
    next_row = []
    last_row = rows[row_num-1]

    for index, num in enumerate(last_row, start=0):
        next_num_index = index+1
        if next_num_index < len(last_row):  # checks if there is a next num
            next_row.append(num + last_row[next_num_index])
    rows.append(add_1s(next_row))

print(rows)
