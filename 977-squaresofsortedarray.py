from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # for i in range(len(nums)-1):
        #     min_index = i
        #     for j in range(i+1, len(nums)):
        #         if nums[j]*nums[j] < nums[min_index]*nums[min_index]:
        #             nums[j], nums[min_index] = nums[min_index], nums[j]
                    
        # return [x*x for x in nums]

        #use built-in sorted function to complete this
        # return sorted([x*x for x in nums]) 

        #use dual pointers to complete this task for the list already sorted
        #either the left or the right element will be the largest after squared
        l, r, i = 0, len(nums) - 1, len(nums) -1 #left and right pointers, i for last element index

        res = [0 for _ in range(len(nums))] #create a list with same length to store result
        while l<=r:
            if nums[l]**2 < nums[r]**2:
                res[i] = nums[r]**2
                r -= 1
            else:
                res[i] = nums[l]**2
                l += 1
            i -= 1 #non-descending order, so i move backwards
        
        return res
  
nums = [-4,-1,0,3,10]
result = Solution().sortedSquares(nums)
print(result)



