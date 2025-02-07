rows = int(input("Enter rows:"))
cols = int(input("Enter columns:"))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        x = int(input("Enter the elements:"))
        row.append(x)
    matrix.append(row)

print(matrix)