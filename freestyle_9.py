
# test_dups = ["zzz", "dog", "bookkeeper", "subdermatoglyphic", "subdermatoglyphics"]
def histogram(st):
    dicki = dict()
    default = 0
    for letter in st:
        dicki[letter] = dicki.get(letter, default)
        dicki[letter] += 1
    return dicki


# name  =  histogram('caracasas')
# print(name)
# nam  =  histogram(['john', 'john', 'john','john', 'mary', 'james'])
# print(nam)



# def has_duplicate(string):
#     h = histogram(string)
#     for key, value in h.items(): # converting the dictionary h into an iterable object with the use of the items method and a tuple of the key and value.
#         if value > 1:   # conditional to check if the string passed in has any repeated values.
#             return True
#     return False


# def loop_test_1():
#     for singleString in test_dups:
#         if has_duplicate(singleString):
#             print(singleString, "has duplicates")
#         else:
#             print(singleString, "has no duplicates")

# page = histogram("catastrophic")
# for index, element in zip(("12345678"), ("banananans")):
#     if element > 1:
#         print(element)# strings
        
        
        
        
        
        
        
# def invert_dict(d):
#     inverse = dict()
#     for key in d:
#         val = d[key]
#         if val not in inverse:
#             inverse[val] = [key]
#         else:
#             inverse[val].append(key)
#         print(inverse)
#     return inverse

# name = histogram('james bond')
# name_1 = histogram('caracas')
# print(name)

# name_inverse = invert_dict(name)
# name_1_inverse = invert_dict(name_1)
# print(name_inverse)
# print(name_1_inverse,"\n")




# name : [animal type, age, sex]
clubs = {
    "Real Madrid": ["League", 34],
    "Barcelona": ["League", 26],
    "Bayern Munich":["League", 26],
    "Liverpool": ["League", 20],
    "Manchester United":["League", 20],
}



print(clubs)
print("")


print("\nPrinting the inverse\n")
def invert(d):
    inverse = dict()
    for key in d:
        val = d[key]
        for item in val:
            if item not in inverse:
                inverse[item] = [key]
            else:
                inverse[item].append(key)

    print(inverse)
    return inverse 


i_clubs = invert(clubs)
print(i_clubs)

print("\n")
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
        print(inverse)
    return inverse


name_1 = histogram('caracas')
name_1_inverse = invert_dict(name_1)
print(name_1_inverse,"\n")





# name : [animal type, age, sex]
animal_shellter = {
    "Teddy": ["dog",4,"male"],
    "Elvis": ["dog",1,"male"],
    "Sheyla": ["dog",5,"female"],
    "Topic": ["hamster",3,"male"],
    "Kuzya": ["cat",10,"male"],
    "Misi": ["cat",8,"female"],
}


print(animal_shellter)
print("")


def invert(d):
    inverse = dict()
    for key in d:
        val = d[key]
        for item in val:
            if item not in inverse:
                inverse[item] = [key]
            else:
                inverse[item].append(key)
    return inverse 


inverted_shellter = invert(animal_shellter)
print(inverted_shellter)




print("Week 7 Learning Journal\n")
# Cluba and Leagues in Europe
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
I was able to achieve this by introducing another for loop inside the already existing for a loop.
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
