def sum (numbers):
    total = 0
    for i in numbers[:4]:
        total += i
    return total


print(sum([1,2,3,3,5,6,7]))



def recursive_sum(numbers):
    if not numbers:
        return 0
    

