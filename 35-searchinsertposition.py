from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        # use binary search to find the target
        while left < right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        # if cannot find the target
        # which means the target is outside the target array
        # then the target should be inserted there
        # so the position of the target should be right
        return right

        # second method - because the array is of distinct integers in ascending order
        # for i in range(len(nums)):
        #   if nums[i] >= target:
        #       return i
        # return len(nums)

nums = [1,3,4,6]
target = 5

result=Solution().searchInsert(nums, target)
print(result)