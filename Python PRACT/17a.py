# for i in range(2,5):
#     for j in range(1,6):
#         print(f"{i}x{j}={i*j}")

cities = ["Mysore","Mangalore","Bangalore","Chickmagalore"]
for city in cities:
    if city == "Bangalore":
        print(f"Found {city}!")
        continue
    else:
        print(city)


for i,city in enumerate(cities):
    print(f"City {i+1}:{city}")


for city in cities:
    print(city)
else:
    print("No cities.")