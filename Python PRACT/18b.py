# Create a dictionary where the keys are Kannada cities, and the values are their populations. Use dictionary comprehension
#  to filter out cities with populations below 10 lakhs.
d = {'Mangalore':76, 'Chickmagalore':23,
     'Bangalore':10, 'Mysore':5}
d1 = {key:value for key, value in d.items() if value<=10}
print(d1)

print(" ")
# Write a Python program that takes a list of lists (a 2D list) as input and:
# Prints the entire matrix row by row.
# Prints the sum of each row in the matrix.

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix)
for row in matrix:
    print(row)
    print(sum(row))