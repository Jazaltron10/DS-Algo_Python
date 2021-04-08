list_of_numbers = [54, 62, 93, 17, 31, 65, 23]

def selection_sort(list):
    sorted_list_of_numbers = []
    
    # print("%-25s %-25s" % (list, sorted_list_of_numbers))
    
    for index in range(0, len(list)):
        index_to_be_moved = index_of_min_number(list)
        sorted_list_of_numbers.append(list.pop(index_to_be_moved))
        # print("%-25s %-25s" % (list, sorted_list_of_numbers))
    return sorted_list_of_numbers

def index_of_min_number(list):
    min_index = 0
    for index in range(1, len(list)):
        if list[index] < list[min_index]:
            min_index = index
    return min_index 

print(selection_sort(list_of_numbers)) 















