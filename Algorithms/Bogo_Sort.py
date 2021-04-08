import random
import sys


def is_sorted(values):
    for index in range(len(values)-1):
        if values[index] > values[index + 1]:
            return False
        return True


def bogo_sort(values):
    while not is_sorted(values):
        random.shuffle(values)
    return values


numbers = [1,3,9,5,8,6]
print(bogo_sort(numbers))
# list_numbers = [54, 62, 93, 17, 31, 65, 23, 32, 98, 20, 79, 69, 89, 26, 27, 22,29, 100, 1, 2, 57, 28, 88, 3, 50, 67, 37, 1, 32, 20, 97]






























