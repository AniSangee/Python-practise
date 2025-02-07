M=[[1,2,3,4],[4,4,5],[6,6,6]]

def remove_duplicate():
    for i in range(len(M)):
        unique=[]
        for j in M[i]:
            if j not in unique:
                unique.append(j)
        M[i]=unique
        print(M[i])

remove_duplicate()