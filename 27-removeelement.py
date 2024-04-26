from typing import List
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         i, l = 0, len(nums)
#         while i < l:
#             if nums[i] == val:
#                 for j in range(i+1, l):
#                     nums[j-1] = nums[j]

#                 l -= 1
#                 i -= 1
#             i += 1
#         return l
nums = [3,2,2,3]
val = 3

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)

        i, j = 0, n-1

        while i<=j:
            while i<=j  and nums[i] != val:
                i += 1
            while i<=j and nums[j] == val:
                j -= 1

            if i < j:
                nums[i] = nums[j]
                i += 1
                j -= 1
        return i

result = Solution().removeElement(nums, val)
print(result)


        