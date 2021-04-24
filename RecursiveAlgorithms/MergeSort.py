List = [250,437,48,830,298,325,222,477,342,74,445,123,432,121,237,213,129,54, 62, 93, 17, 31, 65, 23, 32, 98, 20, 79, 69, 89, 26, 27, 22,29, 100, 1, 2, 57, 28, 88, 3, 50, 67, 37, 1, 32, 20, 97]


def merge_sort(values):
    if len(values)<= 1:
        return values
    
    middle_index = len(values) // 2
    # Now we use the python slice syntax to get the left half of the list
    """
    So basically the merge_sort function just splits any list passed into it when it is being called recursively, be it the right or left list
    """
    
    left_values = merge_sort(values[:middle_index])
    right_values = merge_sort(values[middle_index:])
    print("%15s %-15s" % (left_values, right_values))
    # we'll create a list to hold the sorted values 
    sorted_values = []
    # Now we get to merge the two split halves while sorting them 
    # we'll be moving from left to right 
    left_index = 0  # helps us keep track of our position in the left half of the list
    right_index = 0 # helps us keep track of our position in the right half of the list
    
    # we'll now loop to process all of the values in the list 
    while left_index < len(left_values) and right_index < len(right_values):
        """
        We'll be looking to copy over the lowest values first onto the sorted list
        so first we test whether the value on the left side is less than the value on the right side, if it is, we then copy that value to the sorted list.
        """
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1
    sorted_values += left_values[left_index:] 
    sorted_values += right_values[right_index:] 
    return sorted_values            
    
print(List)
sorted_list = merge_sort(List)
print(sorted_list)