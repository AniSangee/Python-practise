set1 = {"mango","orange","banana","stawberry"}
set2 ={"jack fruits","mango","pomegranets"}

print("Union of set",set1 | set2)
print("Intersection of set",set1 & set2)
print("Difference",set1 - set2)

set1.add("grapes")
print(set1)

print(set1.remove("orange"))
print(set1)

print(set1.discard("orange"))
print(set1)