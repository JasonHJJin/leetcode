# def targetSum(n, arr):

#     def help_targetSum(n, arr, memo):

#         if n in memo:
#             return memo[n]
        
#         memo[n] = help_targetSum(n, arr, memo)

#         return 

#     return help_targetSum(n, arr, {})



# print(targetSum(7, [5, 3, 4, 7]))


def canSum(n, arr):

    if n == 0:
        return True
    
    if n < 0:
        return False
    
    for i in arr:

        remainder = n - i

        if canSum(remainder, arr) == True:
            return True
        
    return False

print(canSum(7, [5, 3, 4, 7]))

def haveSum(n, arr):

    def helpHavesum(n, arr, memo):

        if n in memo:
            return memo[n]
        
        if n == 0:
            return True
        
        if n < 0:
            return False

        for i in arr:

            remainder = n-i
            if canSum(remainder, arr) == True:

                memo[n] = True
                return True
            
        memo[n] = False
        return False
    
    return helpHavesum(n, arr, {})

print(haveSum(200, [5, 3, 4, 7]))

def canConstruct(target, wordbank):


    def help_canConstruct(target, wordbank, memo):

        if target in memo:
            return memo[target]
        if target == '':
            return True
        
        for i in wordbank:
            if target.find(i) == 0:

                suffix = target[len(i):]
                if help_canConstruct(suffix, wordbank, memo) == True:
                    memo[target] = True
                    return True

        memo[target] = False
        return False


    return help_canConstruct(target, wordbank, {})

print(canConstruct("abcdef", ["abc", "d", "ef", "ab"]))