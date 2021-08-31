
# Binary Converter 
def base(num, value):
    if num < 1:
        return value
    else:
        return base((num//2), str(num%2) + value)

print(base( 5, ''))

for i in range(1, 5):
        print("*" * i)
#    for j in range(0, i):



for j in range(1 , 10):
    print("+" * j)

u = 0
while u < 10:
    print("+" * u)
    u+=1


l = 10
while l > 0:
    print("+" * l)
    l-=1


for i in range(1, 5):
    print("Hello")
    for u in range(1, 5):
        print("World")


