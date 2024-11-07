#3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = set(nums) # 3, 0, 1
        
        for i in range(n + 1):
            if i not in s:
                return i
        
#2
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        for i in range(0, len(nums) + 1):
            if i not in seen:
                return i

#1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        for i in range(0, len(nums) + 1):
            if i not in seen:
                return i