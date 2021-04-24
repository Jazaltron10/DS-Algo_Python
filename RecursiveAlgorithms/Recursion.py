def sum (numbers):
    total = 0
    for i in numbers[:4]:
        total += i
    return total


print(sum([1,2,3,3,5,6,7]))


# always add a base case is an alternative to a recursive case
def recursive_sum(numbers):
    if not numbers:
        return 0
    #print("Calling sum(%s)" % numbers[1:])
    remaining_sum = recursive_sum(numbers[1:])
    #print("Call to sum(%s) returning %d + %d" % (numbers, numbers[0], remaining_sum))
    return numbers[0] + remaining_sum


print(recursive_sum([1,2,3,3,5,6,7]))


"""
1. A Recursive Function needs a recursive case that causes it to call itself
2. And it also needs to eventually reach a base case that causes the recursion to stop  
    
"""