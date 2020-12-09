def gridTraveler(n, m, memo={}):
    key = str(n) + ',' + str(m)
    if(key in memo):
        return memo[key]

    if(n == 1 and m == 1):
        return 1
    elif(n == 0 or m == 0):
        return 0

    memo[key] = gridTraveler(n-1, m, memo) + gridTraveler(n, m-1, memo)
    print(memo)
    return memo[key]


print(gridTraveler(3, 3))

# |_S_|___|___|___|
# |___|___|___|___|
# |___|___|___|___|
# |___|___|___|_E_|
