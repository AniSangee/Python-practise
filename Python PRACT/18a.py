# Create a list of 3 dictionaries, where each dictionary contains the name, age, and
#  marks of a student. Loop through the list and print each student's information.
dict1 = {'Name':"Anil", "Age":23, "Marks":80}
dict2 = {'Name':"Amsal", "Age":5, "Marks":90}
dict3 = {'Name':"Sangeetha", "Age":22, "Marks":93}

list = [dict1,dict2,dict3]

l1 = [item for item in list]
print("Student 1",l1[0])
print("Student 2",l1[1])
print("Student 3",l1[2])