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

# Multiplictaion table
s = ""
for i in range(12):
    i+=1
    for j in range(12):
        j +=1
        s += " "+str( i*j)
    print("\n" + s)
    s = ""