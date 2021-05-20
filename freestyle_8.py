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