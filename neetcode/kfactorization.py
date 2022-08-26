"""
Name          : kfactorization.py
Author        : Brian S. Borowski
Version       : 1.1
Date          : March 31, 2018
Last modified : April 5, 2018
Description   : Solution to HackerRank -> Algorithms -> Recursion ->
                K Factorization
                https://www.hackerrank.com/challenges/k-factorization/problem
"""
def k_factorization(n, A):
    def k_factorization_helper(n, A, index):
        if n == 1:
            return [[1]]
        if n == 0 or index >= len(A):
            return [[]]

        result = [[]]
        if n % A[index] == 0:
            use_it = k_factorization_helper(n // A[index], A, index)
            if use_it[0]:
                result = list(map(lambda subset: [A[index]] + subset, use_it))
        lose_it = k_factorization_helper(n, A, index + 1)
        if lose_it[0]:
            if result[0]:
                result = result + lose_it
            else:
                result = lose_it
        return result

    factors = k_factorization_helper(n, sorted(A), 0)
    if not factors[0]:
        return [-1]
    factors.sort(key = lambda subset: len(subset))

    state = 1
    states = []
    for factor in factors[0]:
        states.append(state)
        state *= factor # The last factor is a 1.
    return states

print(k_factorization(6, [5, 2]))
print(k_factorization(12, [4, 5, 6, 3, 2]))
print(k_factorization(72, [2, 4, 6, 9, 3, 7, 16, 10, 5]))
print(k_factorization(200, [10, 20, 200, 4, 2, 25]))
print(k_factorization(231000000, [2, 3, 5, 7, 11, 13, 17, 19]))

if __name__ == '__main__':
    n, _ = input().strip().split(' ')
    n = int(n)
    values = list(map(int, input().strip().split(' ')))
    print(' '.join(map(str, k_factorization(n, values))))
