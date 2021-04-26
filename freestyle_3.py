List =  [54, 62, 93, 17, 31, 65, 23, 32, 98, 20, 79, 69, 89, 26, 27, 22,29, 100, 1, 2, 57, 28, 88, 3, 50, 67, 37, 1, 32, 20, 97]

def quicksort(values):
    if len(values) <= 1:
        return values 
    
    less = []
    greater = []
    pivot = values[0]
    
    for value in values[1:]:
        if value <= pivot:
            less.append(value)
        else:
            greater.append(value)
    return quicksort(less) + [pivot] + quicksort(greater)


sorted_list = quicksort(List)
print(sorted_list)


