class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #compared if the strings are exactly same after sorting
        return sorted(s) == sorted(t)
    
        # list_s = [i for i in s]
        # list_t  = [i for i in t]
        # return sorted(list_s) == sorted(list_t)   
     
s = "anagram"
t = "nagaram"

result = Solution().isAnagram(s, t)
print(result)