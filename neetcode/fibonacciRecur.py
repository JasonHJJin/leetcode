def fiboannci(n):

    def fibo_helper(n, memo):

        if n in memo:
            return memo[n]
        
        if n <= 2:
            return 1

        memo[n] = fibo_helper(n-1, memo) + fibo_helper(n-2, memo)

        return memo[n]

    return fibo_helper(n, {})

print(fiboannci(int(input())))