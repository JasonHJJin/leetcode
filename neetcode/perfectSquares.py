from math import floor, sqrt


def numSquares(self, n: int) -> int:

    maxIndex = floor(sqrt(n)) + 1
    
    output = 0
    remain = 0

    for i in reversed(range(1, maxIndex)):   

        num = i*i


        for j in reversed(range(1, maxIndex)):
            
            if(num * j > n):
                continue
            
            elif (num * j == n):
                return j
            
            elif (num * j < n):
                remain = n - num * j
                if remain >= (j-1)**2:
                    output += 1
                    remain = 0
                
                break

    return output

print(numSquares("",45))