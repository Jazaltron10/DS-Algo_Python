alphabet = "abcdefghijklmnopqrstuvwxyz"
test_dups = ["zzz", "dog", "bookkeeper", "subdermatoglyphic", "subdermatoglyphics"]
test_miss = ["zzz", "subdermatoglyphic", "the quick brown fox jumps over the lazy dog"]


def histogram(string):
    d = dict()
    for char in string:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d


# Part 1
def has_duplicate(string):
    h = histogram(string)
    for k, v in h.items():
        if v > 1:
            return True
    return False


for string in test_dups:
    if has_duplicate(string):
        print(string, "has duplicates")
    else:
        print(string, "has no duplicates")

# Part 2


def missing_letters(string):
    h = histogram(string)
    new_list = []
    #global alphabet
    for char in alphabet:
        if char not in h:
            new_list.append(char)
    return "".join(new_list)


for string in test_miss:
    new_list = missing_letters(string)
    if len(new_list):
        print(string, "is missing letters", new_list)
    else:
        print(string, "uses all letters")