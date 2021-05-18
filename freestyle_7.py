print("Hello world\n\n")


t7 = [[6]]
t5 = [[1, 2], [3], [4, 5, 6],[7,8,9]]
t6 = [[1, 2], [3], [4, 5, 6],[7,8,9]]




def nested_sum(arr):
    
    x = sum(t5.pop(0))
    x2 = sum(t5.pop(0))
    x3 = sum(t5.pop(0))    
    x4 = sum(t5.pop(0))    

    total_sum = x + x2 + x3 + x4
    return total_sum
    
    
    
print(nested_sum(t5))


def nested_sum_2(arr):
    su = 0

    for i in range(len(arr)):
        su += sum(arr.pop(0))
    return su 

print(nested_sum_2(t6))


for fruit in ['a', 'b', 'c', 'd']:
    print(fruit)



mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
print(" ".join(mylist[1::2]))

















