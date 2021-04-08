def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list 

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes O(n log n ) time
    Takes O(n) space
    """

    if len(list)  <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right

    Takes overall O(log n) time
    """

    mid = len(list)//2
    # using the slicing operation has a run time of O(k)
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left,right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in overall O(n) time
    """

    new_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_list.append(left[i])
            i+=1
        else:
            new_list.append(right[j])
            j+=1

    while i < len(left):
        new_list.append(left[i])
        i += 1
    while j < len(right):
        new_list.append(right[j])
        j += 1

    return new_list

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])




alister = [54, 62, 93, 17, 31, 65, 23, 32, 98, 20, 79, 69, 89, 26, 27, 22, 97]
sorted_list = merge_sort(alister)



print(verify_sorted(alister))
print(verify_sorted(sorted_list))
print(sorted_list)




















































































































































































