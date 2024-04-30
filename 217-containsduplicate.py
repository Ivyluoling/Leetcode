from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)

        # return False

        #another way is to compare the length of nums and set(nums)
        #set cannot contain duplicate elements
        return len(nums) != len(set(nums))

nums = [1,1,1,3,3,4,3,2,4,2]

result = Solution().containsDuplicate(nums)
print(result)