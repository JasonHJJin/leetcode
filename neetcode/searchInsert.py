def searchInsert(self, nums, target) -> int:
        
    left = 0
    right = len(nums) - 1

    while(left <= right):

        mid = (left + right) // 2
        
        if target > nums[mid]:

            left = mid + 1
        
        elif target < nums[mid]:

            right = mid - 1
        
        elif target == nums[mid]:

            return mid

    return left


nums = [1,3,5,6] 
target = 10
print(searchInsert("", nums, target))
