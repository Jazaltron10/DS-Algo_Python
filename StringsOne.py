# name = "stop"
# print(name)

# cis = ''
# i = 0 
# while i < len(name):
#     cis += name[i]
#     print(name[i])
#     i+=1
# print(cis)
# print("\n\n")


# cjs = ""
# j = len(name)-1
# # l=0
# while j > -1:
#     cjs += name[j]
#     print(name[j])
#     j-=1
#     # l+=1
# print(cjs)

# if cjs == cis:
#     print("They are equal")
# else:
#     print("They are not equal")
    
    
    
def palindrome(name):
    nor = ""
    rev = ""
    l = 0
    i = 0
    j = len(name) - 1
    
    while l < len(name):
        nor += name[i]
        rev += name[j]
        print(nor, rev)
        i+=1
        j-=1
        if nor == rev:
            # return True
            print("They are equal")
        else:
            # return False
            print("They are not equal")
        l+=1
    print(nor, rev)
    
    
    
# palindrome("1881")
    
# animal = "kangaroo"
def checker(animal):
    # animal = "1881"
    i = len(animal)-1 # last index of the string
    rev = ""
    for s in animal:
        rev += animal[i]    
        i-=1  

    print("The animal is %s", animal)
    print("The reverse is %s", rev)
    # print(rev)
    j = 0
    while j < len(animal):
        if animal[i] == animal[j] and rev == animal:
            print("palindrome")
            return True
        else:
            print("not palindrome")
            return False
    j+=1
    i-=1  
    
    # abcdcba
    
    
faf = checker("abcdcba")
print(faf)
faf = checker("abba")
print(faf)