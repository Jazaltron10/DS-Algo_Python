List = [250,437,48,830,298,325,222,477,342,74,445,123,432,121,237,213,129,54, 62, 93, 17, 31, 65, 23, 32, 98, 20, 79, 69, 89, 26, 27, 22,29, 100, 1, 2, 57, 28, 88, 3, 50, 67, 37, 1, 32, 20, 97]


def Quick_Sort(ListOfValues):
    if len(ListOfValues) <= 1:
        return ListOfValues
    
    lessthananchor = []
    greaterthananchor = []
    anchor = ListOfValues[0]
    
    for Singlevalue in ListOfValues[1:]:
        if Singlevalue <= anchor:
            lessthananchor.append(Singlevalue)
        else:
            greaterthananchor.append(Singlevalue)
            
    return Quick_Sort(lessthananchor) + [anchor] + Quick_Sort(greaterthananchor)

print("The Original Unsorted List of value is ", List , "\n")
NewlySortedList = Quick_Sort(List)
print("The Newly sorted list of value using quicksort is ", NewlySortedList, "\n")