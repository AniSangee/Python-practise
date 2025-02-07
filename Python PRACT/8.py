name=input("Enter your name:")
age = int(input("Enter your age:"))

print("Hello "+name+"! you are",age," years old.")

message = " Python is awesome "
print(message.upper())
print(message.lower())
print(message.replace(" ","_"))
print(message.strip())

txt=input("User text:")
print(txt)
print("Number of character is ",len(txt.replace(" ","")))

text="Hello\n\tworld\n This is python World"
print(text)