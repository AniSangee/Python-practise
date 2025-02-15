def isNumIn(sortedList,target):
    low = 0
    high = len(sortedList)-1

    while low <= high:
        mid = (low + high)//2
        midVal = sortedList[mid]
        if midVal == target:
            return True
        elif midVal < target:
            low = mid + 1
        else:
            high = mid -1
    return False

sortedList = [1,2,3,4,5,6,7,8,9,10]
print(isNumIn(sortedList,7))
print(isNumIn(sortedList,11))
print(isNumIn(sortedList,5))