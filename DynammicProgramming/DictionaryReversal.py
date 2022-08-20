print("Week 7 Learning Journal\n")
# Club and Leagues in Europe
# BreakDown Of My dictionary -> ClubName : [Domestic League Name, Total League Trophies,]
clubs = {
    "Real Madrid": ["La liga", 36],
    "Barcelona": ["La liga", 26],
    "Bayern Munich":["Bundesliga", 26],
    "Juventus":["Serie A", 36],
    "Inter Milan":["Serie A", 20],
    "Liverpool": ["Epl", 20],
    "Manchester United":["Epl", 20],
    "Ajax":["Eredivisie", 36],
}



print("\nPrinting The Original Dictionary")
print(clubs)
# Code Explanation
"""
Below is a modified version of the original inverted function. 
because lists are mutable they cannot be used as keys in a dictionary, and when 
I tried it I kept getting a Type Error like this:
TypeError: unhashable type: 'list'
so I had to come up with a way to access the elements in the list and turn them into keys 
the newly created dictionary.
I was able to achieve this by introducing another for loop inside the already existing for loop.
This new for loop was meant to loop through each item in the value of the original dictionary which is a list 
and while looping through it check to see if the contents of the list are already in the new dictionary, 
if they were not, I would make each element the key in the new dictionary, and since the elements are primitive
data types of string and integer are hashable and can therefore be used as keys in the new dictionary, 
and I would also pass the key of the original dictionary into a list and assign it to the value of the new dictionary.
Now if the element(key) already exists in the new dictionary, I would then append the new values, to the
values(which is a list of the key of the original dictionary) of that key that already exists.
"""
def invert(dictionary):
    inverse = dict()    # creating new inverted dictionary
    for key in dictionary: # looping through original dictionary's keys
        value = dictionary[key] # assigning the value(which is a list) of the original dictionary to a new variable
        for element in value:   # Looping through the value of the original dictionary(which is a list)
            if element not in inverse:  # checking to see if items in list are in the new dictionary
                inverse[element] = [key] # passing the key of original dictionary to a list and assigning it to the value of the new dictionary
            else:
                inverse[element].append(key) # adding the new values(which is a list) that belong to a key that already exists in the new dictionary 

    #print(inverse)
    return inverse   # returning the new dictionary with its key and list of values 


i_clubs = invert(clubs)
print("\n\nPrinting The Inverted Dictionary")
print(i_clubs)   # printing invert dictionary
# Writing the dictionary to an external output file
fout = open('output.txt', 'w')
fout.write("\nThe inverted Dictionary is  ->  %s" % i_clubs)



"""
Describe what is useful about your dictionary. Then describe whether the inverted dictionary is
useful or meaningful, and why.

What is Useful about my dictionary:
My dictionary stores all the names of popular football clubs as the key 
and it stores in a list the various domestic leagues they play in as well 
as their all-time trophies count in winning their league.

What is useful about the Inverted dictionary:
My inverted dictionary is useful because it serves as a filter across all the 
clubs and their respective leagues in the original dictionary.
now with my inverted dictionary, I can see which clubs play in the same league and
also which clubs have the same amount of trophies in their respective leagues.
"""




















































print("\nWK8_LearningJournal\n\n")

def File_Dictionary():
    print("The keys in the dictionary")
    fin = open('input.txt') # creating file object 
    key = fin.readline().strip() # reading first line from file, with no new line
    print(key, type(key)) # printing the data from file and its type 
    newkey = key.split(', ') # converting data from file into a list
    print(newkey[0])    # printing first element of the list newkey
    print(newkey, type(newkey), "\n\n") # printing new list and it's type
    
    
    print("The List of values in the dictionary")
    values = fin.readline().strip() # reading the second line from the input.txt file
    print(values, type(values)) # printing the newly created variable and its type
    newvalues = values.split(', ') # converting the variable to a list
    print(newvalues[0], newvalues[1] ) # printing first and second elements of the newlist
    print(newvalues, type(newvalues),len(newvalues),"\n\n") # printing newlist, its type
    
    
    newlist = [] # creating an empty list to hold lists of values 
    
    i = 0 # used to track index position of first element in newvalues list
    j = 1 # used to track index position of second element in newvalues list
    
    while i < 21:
        # print(i , j)
        """
        Here i just concatenated and appended the first and second elements
        of the newvalues list to the newlist while passing the second element
        into the int() function
        """
        newlist.append([newvalues[i]] + [int(newvalues[j])])
        i +=2 # incrementing the by 2, to take care of the even indexes
        j +=2 # incrementing the by 2, to take care of the odd indexes
    print("The List of values in a list")
    print(newlist, type(newlist),"\n\n\n") # printing the newlist and its type
    
    print("Printing The Original Dictionary")
    """
    Using the zip function and dictionary constructor to create my original dictionary from
    two lists, the newkey list which contains all the keys, and the newlist which contains
    set of list of values.
    """
    original_dictionary = dict(zip(newkey, newlist)) 
    print(original_dictionary, type(original_dictionary)) # printing the original dictionary

    # Passing original dictionary to invert function to be inverted
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

    # assigning return value of invert() function to a new variable and printing it 
    inverted_dictionary = invert(original_dictionary)
    print("\n\nPrinting The Inverted Dictionary")
    print(inverted_dictionary)   # printing inverted dictionary
    fout = open('output.txt', 'w') # creating a file objects, to write to another file
    # using the write method and string formatter to write the inverted dictionary to the
    # output.txt file
    fout.write("The inverted Dictionary is being printed out to the output.txt file \n  ->  %s" % inverted_dictionary)




File_Dictionary()

