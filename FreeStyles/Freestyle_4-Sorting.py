list = [-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]

def sortedSquaredArray(array):
    # Write your code here.
    exponent = []
    newitem = 0
    
    for item in array:
        newitem = item**2
        exponent.append(newitem)
    #exponent.sort()
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







def String_Manipulation():
    print("\nreverse\n")
    word = "realmadrid"
    # print(word[-10])


    i = -1
    while i > - (len(word)+1):
        print(word[i])
        i-=1


    print("\nnormal\n")
    r = 0
    while r < len(word):
        print(word[r])
        r+=1




    word_2 = "manchester_city_UCL"

    a = -1
    print("\nreverse\n")
    while a > -(len(word_2)+1):
        print(word_2[a])
        a-=1

    print("\nnormal\n")

    b = 0
    while b < len(word_2):
        print(word_2[b])
        b+=1



String_Manipulation()








