class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        max = 0
        for i in range(0, len(nums) + 1):
            if i not in seen:
                return i