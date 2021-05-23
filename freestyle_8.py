import random

# A Single Random Number generator
# The random() method in random module generates a float number between 0 and 1.
randNum_1 = random.random()
print(randNum_1)



#Generating number in a range 
# The randint() method generates a integer between a given range of numbers
randNum_2 = random.randint(0, 10)
print(randNum_2)


# Generating a list of numbers using the for loop() 
"""We can use the above randint() method along with a for loop to generate a list of numbers. We first create an empty list and then append the random numbers generated to the empty list one by one."""
randomList = []
for i in range(0, 5):
    n = random.randint(1, 30)
    randomList.append(n)
    # print(randomList)
print(randomList)
    

# Using random.sample()
"""We can also use the sample() method available in random module to directly generate a list of random numbers.Here we specify a range and give how many random numbers we need to generate."""
#Generate 5 random numbers between 10 and 30
randomlist_2 = []
randomlist_2 = random.sample(range(10, 30), 5)
print(randomlist_2)




# Binary Search
ArrayList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
def binary_search(array, value):
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound)//2
        value_at_midpoint = array[midpoint]
        if value < value_at_midpoint:
            upper_bound = midpoint - 1
        elif value > value_at_midpoint:
            lower_bound = midpoint + 1
        elif value == value_at_midpoint:
            return midpoint
    return None

print("Target found at index ",binary_search(ArrayList, 'a'))

# Linear Search
def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

print("The index for this Linear search is  ",linear_search(ArrayList, 'k'))






# Binary Converter 
def base(num, value):
    if num < 1:
        return value
    else:
        return base((num//2), str(num%2) + value)

print(base( 5, ''))

for i in range(1, 5):
        print("*" * i)
#    for j in range(0, i):



for j in range(1 , 10):
    print("+" * j)

u = 0
while u < 10:
    print("+" * u)
    u+=1


l = 10
while l > 0:
    print("+" * l)
    l-=1


for i in range(1, 5):
    print("Hello")
    for u in range(1, 5):
        print("World")



arr = [1, 2, 3, 4, 5, 6, 7, 8]

def binarySearch(array, target):
    # Write your code here.

	first = 0
	last = len(array) - 1
	
	while first <= last:
		mindex = (first + last)//2
		midpoint = array[mindex]
		if target == midpoint:
			return mindex
		elif target > midpoint:
			first = mindex + 1
		else: 
			last = mindex - 1
		if target not in array:
			return -1


print(binary_search(arr, 8))





numbers = [1,2,3,4,5,6,7,8,9,10]
list_names = ['david', 'john', 'mary', 'damien']

name = input()

def List_String_Search(list, target):
    """
    prints target founnd and the index it was found at else prints not in list
    """
    for i in range(0, len(list)):
        if list[i] == target:
            print(list[i], " is in the list at index ", i)
    print(target, 'not in list')

        

List_String_Search(list_names, name)
        