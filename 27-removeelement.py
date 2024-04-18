from typing import List
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         for i in range(1, len(nums)):
            
#             if nums[i] == val:
#                 pass
#             else:
#                 nums[0]=nums[i]
#                 nums[i]=nums[0]
        
#         return nums
    
nums = [3,2,2,3]
val = 3

# result = Solution().removeElement(nums, val)
# print(result)

for i in range(0, len(nums)):
    if nums[i] == val:
        for j in range(i+1, len(nums)): 
            nums[j-1] = nums[j]
            nums[j] = nums[i]
        i += 1
        

        
print(nums)
        