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


print(fib(1))
# print(fibonacci(40))


# memo = {0:0}
def fibay(n, memo = dict() ):
    if n in memo: return memo[n]
    if n <= 2: return 1
    
    res = fibay(n-1, memo) + fibay(n-2, memo)
    memo[n] = res
    print(memo)
    return res


print(fibay(5))
# print(fibay(8))
# print(fibay(13))
# print(fibay(20))
# print(fibay(50))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(4))