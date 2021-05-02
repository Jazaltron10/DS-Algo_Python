list = [-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]

def sortedSquaredArray(array):
    # Write your code here.
    exponent = []
    newitem = 0
    
    for item in array:
        newitem = item**2
        exponent.append(newitem)
    
    return exponent

	
newlist = sortedSquaredArray(list)
print(newlist)


def quicksort(newlist):
    if len(newlist) <= 1:
        return newlist
    
    lesser = []
    greater = []
    pivot = newlist[0]
    
    
    for anitem in newlist[1:]:
        if anitem <= pivot:
            lesser.append(anitem)
        else:
            greater.append(anitem)
    return quicksort(lesser) + [pivot] + quicksort(greater)


print(quicksort(newlist))






# This is some code for the Ackerman Function 
def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))


Ackerman_Function = ack(3,4)
print(Ackerman_Function)

















