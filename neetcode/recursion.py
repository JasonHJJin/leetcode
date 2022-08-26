"""
Recursion, 'use it or lose it', memoization
Created on July 26, 2022
@author: Brian Borowski
"""

def factorial(n):
    """Computes the factorial of a number using linear recursion."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fact_tail(n):
    """Computes the factorial of a number using tail recursion."""
    def fact_tail_helper(n, accum):
        if n == 0:
            return accum
        return fact_tail_helper(n - 1, n * accum)
    return fact_tail_helper(n, 1)

# Test factorial functions.
for n in range(10):
    print(factorial(n), fact_tail(n))

# def fib(n):
#     """Computes the nth Fibonacci number using tree recursion."""
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)

# # Test fib function, but larger values of n take a long time to compute.
# for n in range(40):
#     print(n, fib(n))

# def fib_memo(n):
#     """Computes the nth Fibonacci number using memoized tree recursion."""
#     def fib_memo_helper(n, memo):
#         # If key is in memo, return memo[key]
#         if n in memo:
#             return memo[n]
#         # Do work with recursion, storing the
#         # result in a local variable
#         if n <= 1:
#             result = n
#         else:
#             result = fib_memo_helper(n - 1, memo) + \
#                      fib_memo_helper(n - 2, memo)
#         # Store the result in the memo and return the result
#         memo[n] = result
#         return result
#     return fib_memo_helper(n, {})

# # Test fib_memo function, which should execute very quickly, even for large
# # values of n.
# for n in range(40):
#     print(n, fib_memo(n))

# def powerset(lst):
#     """Returns the power set of the list, that is, the set of all subsets of the
#     list."""
#     if lst == []:
#         return [[]]
#     lose_it = powerset(lst[1:])
#     use_it = list(map(lambda subset: [lst[0]] + subset, lose_it))
#     return lose_it + use_it

# print(powerset(['a', 'b', 'c']))

# def subset(target, lst):
#     """Determines whether or not it is possible to create target sum using the
#     values in the list. Values in the list can be positive, negative or zero."""
#     if target == 0:
#         return True
#     if lst == []:
#         return False
#     return subset(target - lst[0], lst[1:]) or \
#            subset(target, lst[1:])

# def subset_with_values(target, lst):
#     """Determines whether or not it is possible to create the target sum
#     using values in the list. Values in the list can be positive, negative, or
#     zero. The function returns a tuple of exactly two items. The first is a
#     Boolean that indicates True if the sum is possible and False if it's not.
#     The second element in the tuple is a list of all the values that add up
#     to make the target sum."""
#     if target == 0:
#         return (True, [])
#     if lst == []:
#         return (False, [])
#     use_it = subset_with_values(target - lst[0], lst[1:])
#     if use_it[0]:
#         return (True, [lst[0]] + use_it[1])
#     return subset_with_values(target, lst[1:])

# print(subset_with_values(5, [3, 1, 2]))

# def LCS(s1, s2):
#     """Returns the length of the longest common subsequence in strings s1 and s2."""
#     if s1 == '' or s2 == '':
#         return 0
#     if s1[0] == s2[0]:
#         return 1 + LCS(s1[1:], s2[1:])
#     return max(LCS(s1, s2[1:]), LdCS(s1[1:], s2))

# print(LCS('sam', 'apartment'))

# def LCS_with_values(s1, s2):
#     """Returns a tuple of the length of the longest common subsequence in strings s1 and s2
#     as well as the string of characters that in that subsequence."""
#     if s1 == '' or s2 == '':
#         return (0, '')
#     if s1[0] == s2[0]:
#         result = LCS_with_values(s1[1:], s2[1:])
#         return (1 + result[0], s1[0] + result[1])
#     useS1 = LCS_with_values(s1, s2[1:])
#     useS2 = LCS_with_values(s1[1:], s2)
#     if useS1[0] > useS2[0]:
#         return useS1
#     return useS2

# print(LCS_with_values('sam', 'apartment'))
