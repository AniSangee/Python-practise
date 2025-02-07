# def addToSum(a,b): 
#     sum = a + b   #local variables
#     print(sum)

# addToSum(2,8)   
# addToSum(5,3)


name = "Global variable"
def var():
    name = "Local variable"
    print(name)

var()
print(name)