lst = ['act','atc','cat','dog','god']
lst1 = []

while lst:
    word = lst[0]
    group = [w for w in lst if sorted(w) == sorted(word)]
    lst1.append(group)

    for w in group:
        lst.remove(w)
print(lst1)
