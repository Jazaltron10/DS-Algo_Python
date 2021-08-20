message = "Welcome to Classes"
print("\n" + message)
message.upper()
print("\n" + message.upper() )


while True:
    if message.startswith("W"):
        print("\n" + message)
    break;


# fibonacci using memos
known = {0:0, 1:1}
def fib(n):
    if n in known:
        #print(known)    
        return known[n] 
    
    res = fib(n-1) + fib(n-2) 
    #print("%s" % res)
    known[n] = res 
    # print(known[n])
    return res 


print(fib(50))
# print(fibonacci(40))