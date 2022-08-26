import time

def maxdepth(n):

    def helper(n, memo):
        
        return helper(n, memo)

    return helper(n, {})


start_time = time.time()
maxdepth()