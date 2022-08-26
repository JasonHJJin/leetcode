def gridTraveler(x, y):

    def help_gridTraveler(x, y, memo):

        key = (x, y)
        
        if key in memo:
            return memo[key]
        
        if x == 0 or y == 0:
            return 0
        if x == 1 and y == 1:
            return 1
        
        memo[key] = help_gridTraveler(x-1, y, memo) + help_gridTraveler(x, y-1, memo)

        return memo[key]

    return help_gridTraveler(x, y, {})



print(gridTraveler(2, 3))
print(gridTraveler(8, 8))
print(gridTraveler(18, 18))