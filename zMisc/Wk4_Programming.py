
"""
a is a power of b 
if a is divisible by b 

and also a/b is a power of b
"""

def is_divisible(x,y):
    return  x % y == 0


def is_power(a,b):
    if is_divisible(a,b):
        print("hello world")
    else:
        print("my name is")
    
    

# is_power(5,6)


# Fermat Theorem 1

# a = int(input())
# b = int(input())
# c = int(input())
# n = int(input())


def check_fermat(a,b,c,n):
    if n >= 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")


# check_fermat(a,b,c,n)



"""
# The Triangle
side_a = int(input())
side_b = int(input())
side_c = int(input())

def is_triangle(a, b, c):
    if (a > b + c) and (b < a + c) and (c > a + b):
        print("NO, you can't form a triangle ")
    else: 
        print("YES, a triangle can be formed ")
        
        
is_triangle(side_a, side_b, side_c)
"""

# The Recursion Exercise 


list =[54, 62, 93, 17, 31, 65, 23]

# This is another quicksort attempt 

def quickie(list):
    if len(list) <= 1:
        return list 
    
    lesser = []
    greater = []
    pivot = list[0]
    
    
    for item in list[1:]:
        if item <= pivot:
            lesser.append(item)
        else:
            greater.append(item)
    
    return quickie(lesser) + [pivot] + quickie(greater)


print(quickie(list))




def merge(list):
    if len(list) <= 1:
        return list
    
    mindex = len(list)//2
    
    lside = merge(list[:mindex])
    rside = merge(list[mindex:])
    
    sorted_list = []
    lindex = 0 # this keeps track of the positional index on the left side of the list 
    rindex = 0 # this keeps track of the positional index on the right side of the list 
    
    
    while lindex < len(lside) and rindex < len(rside):
        if lside[lindex] < rside[rindex]:
            sorted_list.append(lside[lindex])
            lindex +=1
        else:
            sorted_list.append(rside[rindex])
            rindex +=1
    
    sorted_list += lside[lindex:]
    sorted_list += rside[rindex:]
    return sorted_list

print(merge(list))


n = 10
while n != 1:
    print (n,end=' ')
    if n % 2 == 0:        # n is even
        n = n // 2
    else:                # n is odd
        n = n * 3 + 1
        
        
        


print ("%s %d %f" % (5, 5, 5))