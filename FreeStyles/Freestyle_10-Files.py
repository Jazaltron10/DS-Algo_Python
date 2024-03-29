"""
# This Section deals with files 
import math

table = [5]

def bsearch(sorted_table, element):
    index = math.ceil(len(sorted_table)/2)

    while element != sorted_table[index]:
        if sorted_table[index] > element:
            index = math.ceil(index/2)
        else:
            index = math.ceil(index + index / 2)

    return index


print(bsearch(table, 5))
"""



# A Brute force Solution To The Problem
def write_file_4():
    fin = open('input.txt')
    key = fin.readline().strip()
    print(key, type(key))
    newkey = key.split(', ')
    print(newkey[0])
    print(newkey, type(newkey), "\n")
    
    
    
    values = fin.readline().strip()
    print(values, type(values))
    newvalues = values.split(', ')
    print(newvalues[0], newvalues[1] )
    print(newvalues, type(newvalues),len(newvalues),"\n")


    newlist = []
    club1 = []
    club1.append(newvalues[0])
    club1.append(int(newvalues[1]))
    print(club1, type(club1))
    
    club2 = []
    club2.append(newvalues[2])
    club2.append(int(newvalues[3]))
    print(club2, type(club2))
    
    club3 = []
    club3.append(newvalues[4])
    club3.append(int(newvalues[5]))
    print(club3, type(club3))
    
    club4 = []
    club4.append(newvalues[6])
    club4.append(int(newvalues[7]))
    print(club4, type(club4))
    
    club5 = []
    club5.append(newvalues[8])
    club5.append(int(newvalues[9]))
    print(club5, type(club5))
    
    club6 = []
    club6.append(newvalues[10])
    club6.append(int(newvalues[11]))
    print(club6, type(club6))
    
    club7 = []
    club7.append(newvalues[12])
    club7.append(int(newvalues[13]))
    print(club7, type(club7))
    
    club8 = []
    club8.append(newvalues[14])
    club8.append(int(newvalues[15]))
    print(club8, type(club8))
    
    
    newlist.append(club1)
    newlist.append(club2)
    newlist.append(club3)
    newlist.append(club4)
    newlist.append(club5)
    newlist.append(club6)
    newlist.append(club7)
    newlist.append(club8)
    print(newlist, type(newlist),"\n\n\n")
    
    original_dictionary = dict(zip(newkey, newlist))
    print(original_dictionary, type(original_dictionary))

    def invert(dictionary):
        inverse = dict()   
        for key in dictionary:
            value = dictionary[key]
            for element in value:  
                if element not in inverse:  
                    inverse[element] = [key]
                else:                           
                    inverse[element].append(key)

        #print(inverse)
        return inverse  

    inverted_dictionary = invert(original_dictionary)
    print("\n\nPrinting The Inverted Dictionary")
    print(inverted_dictionary)   
    fout = open('test.txt', 'w')
    fout.write("The inverted Dictionary is being printed out to the test.txt file \n  ->  %s" % inverted_dictionary)


write_file_4()



# A much more optimised Solution to the problem 
def test():
    fin = open('input.txt')
    key = fin.readline().strip()
    print(key, type(key))
    newkey = key.split(', ')
    print(newkey[0])
    print(newkey, type(newkey), "\n")
    
    
    
    values = fin.readline().strip()
    print(values, type(values))
    newvalues = values.split(', ')
    print(newvalues[0], newvalues[1] )
    print(newvalues, type(newvalues),len(newvalues),"\n")
    
    
    newlist = []
    
    i = 0
    j = 1
    print(newlist)
    while i < 15:
        print(i , j)
        newlist.append([newvalues[i]] + [int(newvalues[j])])
        i +=2
        j +=2
    print(newlist, type(newlist),"\n\n\n")
    
    print("Printing The Original Dictionary")
    original_dictionary = dict(zip(newkey, newlist))
    print(original_dictionary, type(original_dictionary))

    def invert(dictionary):
        inverse = dict()   
        for key in dictionary:
            value = dictionary[key]
            for element in value:  
                if element not in inverse:  
                    inverse[element] = [key]
                else:                           
                    inverse[element].append(key)

        #print(inverse)
        return inverse  

    inverted_dictionary = invert(original_dictionary)
    print("\n\nPrinting The Inverted Dictionary")
    print(inverted_dictionary)   
    fout = open('test.txt', 'w')
    fout.write("The inverted Dictionary is being printed out to the test.txt file \n  ->  %s" % inverted_dictionary)



test()
    
    
    
    

# A Brute force Solution To The Problem
def write_file_4():
    fin = open('input.txt')
    key = fin.readline().strip()
    print(key, type(key))
    newkey = key.split(', ')
    print(newkey[0])
    print(newkey, type(newkey), "\n")
    
    
    
    values = fin.readline().strip()
    print(values, type(values))
    newvalues = values.split(', ')
    print(newvalues[0], newvalues[1] )
    print(newvalues, type(newvalues),len(newvalues),"\n")


    newlist = []
    club1 = []
    club1.append(newvalues[0])
    club1.append(int(newvalues[1]))
    print(club1, type(club1))
    
    club2 = []
    club2.append(newvalues[2])
    club2.append(int(newvalues[3]))
    print(club2, type(club2))
    
    club3 = []
    club3.append(newvalues[4])
    club3.append(int(newvalues[5]))
    print(club3, type(club3))
    
    club4 = []
    club4.append(newvalues[6])
    club4.append(int(newvalues[7]))
    print(club4, type(club4))
    
    club5 = []
    club5.append(newvalues[8])
    club5.append(int(newvalues[9]))
    print(club5, type(club5))
    
    club6 = []
    club6.append(newvalues[10])
    club6.append(int(newvalues[11]))
    print(club6, type(club6))
    
    club7 = []
    club7.append(newvalues[12])
    club7.append(int(newvalues[13]))
    print(club7, type(club7))
    
    club8 = []
    club8.append(newvalues[14])
    club8.append(int(newvalues[15]))
    print(club8, type(club8))
    
    
    newlist.append(club1)
    newlist.append(club2)
    newlist.append(club3)
    newlist.append(club4)
    newlist.append(club5)
    newlist.append(club6)
    newlist.append(club7)
    newlist.append(club8)
    print(newlist, type(newlist),"\n\n\n")
    
    original_dictionary = dict(zip(newkey, newlist))
    print(original_dictionary, type(original_dictionary))

    def invert(dictionary):
        inverse = dict()   
        for key in dictionary:
            value = dictionary[key]
            for element in value:  
                if element not in inverse:  
                    inverse[element] = [key]
                else:                           
                    inverse[element].append(key)

        #print(inverse)
        return inverse  

    inverted_dictionary = invert(original_dictionary)
    print("\n\nPrinting The Inverted Dictionary")
    print(inverted_dictionary)   
    fout = open('test.txt', 'w')
    fout.write("The inverted Dictionary is being printed out to the test.txt file \n ->  %s" % inverted_dictionary)


write_file_4()



# A much more optimised Solution to the problem 
def test():
    fin = open('input.txt')
    key = fin.readline().strip()
    print(key, type(key))
    newkey = key.split(', ')
    print(newkey[0])
    print(newkey, type(newkey), "\n")
    
    
    
    values = fin.readline().strip()
    print(values, type(values))
    newvalues = values.split(', ')
    print(newvalues[0], newvalues[1] )
    print(newvalues, type(newvalues),len(newvalues),"\n")
    
    
    newlist = []
    
    i = 0
    j = 1
    print(newlist)
    while i < 15:
        print(i , j)
        newlist.append([newvalues[i]] + [int(newvalues[j])])
        i +=2
        j +=2
    print(newlist, type(newlist),"\n\n\n")
    
    print("Printing The Original Dictionary")
    original_dictionary = dict(zip(newkey, newlist))
    print(original_dictionary, type(original_dictionary))

    def invert(dictionary):
        inverse = dict()   
        for key in dictionary:
            value = dictionary[key]
            for element in value:  
                if element not in inverse:  
                    inverse[element] = [key]
                else:                           
                    inverse[element].append(key)

        #print(inverse)
        return inverse  

    inverted_dictionary = invert(original_dictionary)
    print("\n\nPrinting The Inverted Dictionary")
    print(inverted_dictionary)   
    fout = open('test.txt', 'w')
    fout.write("The inverted Dictionary is being printed out to the test.txt file \n  ->  %s" % inverted_dictionary)



test()



    
    
    
    
    
    # ileft =[]
    # jright =[]
    # lisad = [1, '2', 3, '4', 5, '6', 7, '8']
    # plisa = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # while i < 8:
    #     print(i , j)
    #     complicado = ileft + jright
    #     ileft.append([newvalues[i]])
    #     jright.append([int(newvalues[j])])

    #     i +=2
    #     j +=2
    
    # print(complicado)
    
    
    
    
    
    