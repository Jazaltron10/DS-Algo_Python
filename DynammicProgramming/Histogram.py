# Dictionary as a collection of counters 
def histogram(aString):
    dictionary = dict()
    for character in aString:
        if character not in dictionary:
            dictionary[character] = 1
        else:
            dictionary[character]+=1
    return dictionary

# print(histogram('the quick brown fox jumps over the lazy dog'))
print(histogram("banabas"))
h = histogram("banaraskas")
print(h)
print(h.get('a', 0))

# Second Histogram Algorithm
def histo(aGivenString):
    dictionary = dict()
    defaultValue = 0 # gets returned if the key does not have any value in the dictionary
    for letter in aGivenString:
        dictionary[letter] = dictionary.get(letter, defaultValue)
        dictionary[letter] += 1
    return dictionary

print(histo('bananas'))

