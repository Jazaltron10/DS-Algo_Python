print("La Sectiona De DickiShionarey\n")

# Starting 
eng2sp = dict()
print(eng2sp)

# We use the square brackets to add items to a dictionary 
eng2sp['one'] = 'uno'  # creates a line that maps from the key 'one' to the value 'uno'
print(eng2sp)


eng2fr = {'one':'un','two':'deux','three':'trois','four':'quatre','five':'cinq'}
print(eng2fr)

# Elements in a dictionary are not indexed with integer indices, instead they use the key to look up corresponding values
# print(eng2sp['four']) # gives a key error because this key does not exist
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'

print(eng2sp) 

# checking the length of a dictionary 
print("The length of the eng2sp dictionary is" , len(eng2sp))
print("The length of the eng2fr dictionary is",len(eng2fr))

# To check If a key exists in a dictionary you use the "in" Keyword 
print('one' in eng2sp,'four' in eng2sp)

# To check if a value exist within a dictionary 
# You would have to go through two step process 
# First process = you use the values method onthe dictionary and assign it to a variable {This returns a collection of the values}
# Second process = you then use the "in" operator 

vals = eng2sp.values()
vals_2 = eng2fr.values()
print('uno' in vals, 'cinq' in vals, 'cinq' in vals_2)  



# Dictionary as a collection of counters 
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c]+=1
    return d

# print(histogram('the quick brown fox jumps over the lazy dog'))
print(histogram("banabas"))
h = histogram("banaraskas")
print(h)
print(h.get('a', 0))

def histo(st):
    dicki = dict()
    default = 0
    for letter in st:
        dicki[letter] = dicki.get(letter, default)
        dicki[letter] += 1
    return dicki

print(histo('bananas'))


# Looping and Dictionaries 
# Mind you h is a string that has been transformed to a dictionary after going through the histogram function
def print_hist(h):
    for key in sorted(h): # we use the sorted method if you want the keys printed to be sorted in ascending order
        print(key, h[key])
        
        
print_hist(histo('madagaskar'))        





# Reverse Lookup 
# This is basically a way of finding the first key that maps to a particular value in a given dictionary

def reverse_lookup(d , v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError("The value does not appear in the dictionary")# raise statement causes an exception
    
    
dicki_1 = histogram('parrot')
dicki_2 = histogram('parrotaraskoh')
dicki_3 = histogram('moggot robinho')
dicki_4 = histogram('Kendrick Kungfu Kdot Kenny K')


# Example of a successful reverse_lookup
key_1 = reverse_lookup(dicki_1, 2)
key_2 = reverse_lookup(dicki_2, 3)
key_3 = reverse_lookup(dicki_3, 4)
key_4 = reverse_lookup(dicki_4, 5)

print(key_1,key_2,key_3, key_4)

# Dictionaries and Lists 
# Lists can appear as values in a dictionary. 
# For example, if you are given a dictionary that maps 
# from letters to frequencies, 
# you might want to invert it; that is, create a dictionary that maps 
# from frequencies to letters. 
# Since there might be several letters with the same frequency, 
# each value in the inverted dictionary should be a list of letters

# Below is a function that inverts a dictionary

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

name = histogram('james bond')
name_1 = histogram('caracas')
print(name)

name_inverse = invert_dict(name)
name_1_inverse = invert_dict(name_1)
print(name_inverse)
print(name_1_inverse)












