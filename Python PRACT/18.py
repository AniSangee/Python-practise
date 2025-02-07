# Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.
foods = ['chapathi','rotti','dose','idli','uppit']
print(foods)
foods1 = [food.upper() for food in foods]

print(foods1)

# Create a dictionary of 5 items with their prices. Write a program that
#  calculates the total price of all items using a for loop.

dict = {'book':30, 'pen':10, 'pencil':7, 'rubber':5, 'sharpner':4}
total = 0
for i, item in dict.items():
    total+=item
print("Sum =",total)

# Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.
l =[num for num in range(1,11)]
print(l)

l1 =[num**2 for num in l]
print("Squares=",l1)
