# Write a for loop that prints all multiples of 3 between 1 and 30.

for i in range(1,31):
    if i%3 == 0:
        print(i)

# Write a program using a for loop that calculates the sum of numbers from 1 to 10.
sum=0
for i in range(1,11):
    sum=sum+i
print("\nSum=",sum)

# Write a program that takes your name as input and prints each letter of your name using a for loop.
name =input("Enter your name:")

for letter in name:
    print(letter)
 

# Write a program that counts how many vowels are in a given string using a for loop.
text = input("Enter the text:")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count+=1
print(count)
