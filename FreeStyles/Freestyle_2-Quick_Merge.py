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




List =  [54, 62, 93, 17, 31, 65, 23, 32, 98, 20, 79, 69, 89, 26, 27, 22,29, 100, 1, 2, 57, 28, 88, 3, 50, 67, 37, 1, 32, 20, 97]


def merge(values): # type: ignore
    if len(values) <= 1:
        return values
    
    mindex = len(values) // 2
    
    left_side = merge(values[:mindex])
    right_side = merge(values[mindex:])
    
    sorted_list = []
    
    lindex = 0 # this keeps track of the positional index on the left side 
    rindex = 0 # this keeps track of the positional index on the right side
    
    while lindex < len(left_side) and rindex < len(right_side):
        if left_side[lindex] < right_side[rindex]:
            sorted_list.append(left_side[lindex])
            lindex += 1
        else:
            sorted_list.append(right_side[rindex])
            rindex += 1
    sorted_list += left_side[lindex:]
    sorted_list += right_side[rindex:]
    return sorted_list


final_list = merge(List)
print(final_list)            
        
    
    
    
    
    




List =  [54, 62, 93, 17, 31, 65, 23, 32, 98, 20, 79, 69, 89, 26, 27, 22,29, 100, 1, 2, 57, 28, 88, 3, 50, 67, 37, 1, 32, 20, 97]



def merge(values):
    if len(values) <= 1:
        return values
    
    mindex = len(values) // 2
    
    left_side = merge(values[:mindex])
    right_side = merge(values[mindex:])
    
    sorted_list = []
    
    lindex = 0 # this keeps track of the positional index on the left side 
    rindex = 0 # this keeps track of the positional index on the right side
    
    while lindex < len(left_side) and rindex < len(right_side):
        if left_side[lindex] < right_side[rindex]:
            sorted_list.append(left_side[lindex])
            lindex += 1
        else:
            sorted_list.append(right_side[rindex])
            rindex += 1
    sorted_list += left_side[lindex:]
    sorted_list += right_side[rindex:]
    return sorted_list


final_list = merge(List)
print(final_list)            
        
""" def mergesort(values):
    if len(values) <= 1:
        return values

    mindex = len(values)//2

    leftside = mergesort(values[:mindex])
    rightside = mergesort(values[mindex:])


    sorted_list = []

    lindex = 0 # this helps to keep track of the index position on the leftside 
    rindex = 0 # this helps to keep track of the index position on the rightside 

    while lindex < len(leftside) and rindex < len(rightside):
        if leftside[lindex] < rightside[rindex]:
            sorted_list.append(leftside[lindex])
            lindex += 1
        else:
            sorted_list.append(rightside[rindex])
            rindex += 1
    sorted_list += leftside[lindex:]
    sorted_list += rightside[rindex:]
    return sorted_list


final_list = mergesort(List)
print(final_list) """

