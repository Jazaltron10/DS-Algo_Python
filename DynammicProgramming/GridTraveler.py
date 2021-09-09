def gridTraveler(m,n,memo=dict()):
    key = str(m) + "," + str(n)
    # print(key)
    
    if key in memo: return memo[key]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    
    res = gridTraveler(m-1,n,memo)+gridTraveler(m,n-1,memo)
    memo[key] = res
    # print(memo)
    return res
    
    
    
# print(gridTraveler(1,1))
# print(gridTraveler(2,3))
# print(gridTraveler(3,2))
# print(gridTraveler(3,3))
# print(gridTraveler(18,18))
# print(gridTraveler(32,20))


# APPROACH TWO
memo_2 = {}
def gridTraveler_2(m,n):
    key = str(m) + "," + str(n)
    if key in memo_2:
        return memo_2[key]
    
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    res = gridTraveler_2(m-1,n)+gridTraveler_2(m,n-1)
    memo_2[key] = res
    # print(memo_2)
    return res
# print(gridTraveler_2(1,1))
# print(gridTraveler_2(2,3))
# print(gridTraveler_2(3,2))
# print(gridTraveler_2(3,3))
print(gridTraveler_2(18,18))
# print(gridTraveler_2(32,20))
# print(gridTraveler_2(45,90))




# names = dict()
names = {"james":"john", "mary":"connor"}
print(names["james"])