karnataka_dish ={
    "Chikmaglore":"Coffee",
    "Mangalore":"Fish meals",
    "Bangalore":"Ckn Burger",
    "Udupi":"Idli",
    "Mysore":"Mysore Pk"
}

print(karnataka_dish)
print(type(karnataka_dish))
karnataka_dish["Dharawad"] = "Pheda"
karnataka_dish["Bangalore"] = "ckn Biriyani"
del karnataka_dish["Mysore"]
print(karnataka_dish)
print(karnataka_dish.keys())
print(karnataka_dish.values())