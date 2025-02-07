# Bus pass
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age <= 5:
    print(name,"you have free bus pass.")
elif age >=60:
        print(name,"you have senior citizen discount.")
else:
    print(name,"you should pay full price")

# Library membership
if age <= 18:
    print(name,"you get student membership.")
elif age >=60:
    print(name,"you get senior citizen membership.")
else:
    print(name,"you get regular membership")