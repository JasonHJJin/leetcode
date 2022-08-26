from ast import List


def threeSum(self, nums):

        i = 0
        j = 1
        k = 2

        int(i)
        int(j)
        int(k)

        res = set()

        for i in range(len(nums)-2):
            
            for j in range(i+1, len(nums)-1):
                
                for k in range(j+1, len(nums)):
                    
                    if nums[i] + nums[j] + nums[k] == 0:
                        
                        res.add((nums[i],nums[j],nums[k]))                        

        
        return list(res)

                

print(threeSum("", [-1,0,1,2,-1,-4]))