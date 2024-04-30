from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # #my initial thought
        # sum = 0
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         sum = nums[i] + nums[j]
        #         if sum == target:
        #             return i, j

        #another method is to find the complement of the element to the target
        nums_dict = {} #create a dictionary to store complements and the index of the element

        # for i, num in enumerate(nums):

        #     complement = target - num

        #     if complement in nums_dict:
        #         return [nums_dict[complement], i]
            
        #     nums_dict[num] = i

        for i , num in enumerate(nums):
            if num in nums_dict: #check if the current number matches any complement in dict
                return [nums_dict[num], i] #if fount, return the index stored as the value and the current index
            
            complement = target - num #calculate the complement of the element

            nums_dict[complement] = i #store the index with the complement as the value

nums = [2,7,11,15]
target = 9

result = Solution().twoSum(nums, target)
print(result)