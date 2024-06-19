def TwoNumberSum(arr, target):
    twonums = []
    
    i = 0
    for i in range(len(arr)):
        j = i+1
        for j in range(len(arr)):
            sum = arr[i] + arr[j]
            if sum == target:
                twonums.append(arr[i])
                twonums.append(arr[j])
    return twonums
            
    # return []




# arr = [3,5,-4,8,11,1,-1,6]
# target = 10
# res = TwoNumberSum(arr, target)
# print(res)
def twons(ar, tar):
    twonums = []
    a = 0
    while a < len(ar):
        b = a+1
        while b < len(ar):
            sum = ar[a] + ar[b]
            # print(sum)
            if sum == tar:
                twonums.append(ar[a])
                twonums.append(ar[b])
                return twonums
            b+=1
        a+= 1
    return []    
            
            
ar = [3,5,-4,8,11,1,-1,6]
target = 100
res = twons(ar, target)
print(res)



    
    
def palindrome(string):
    i = len(string)-1 # last index of the string
    j = 0
    print("The string is a %s" % (string))
    while j < len(string):
        if string[i] != string[j]: #and rev == name:
            print("not palindrome")
            return False
        j+=1
        i-=1      
        
    print("palindrome")
    return True    
    
    
    
faf = palindrome("abcdcba")
print(faf, "\n")
faf = palindrome("abbaQ")
print(faf)    
    
    
    

    


