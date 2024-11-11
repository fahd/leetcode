class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = dict({0:-1})
        curr = ans = 0
        for i, num in enumerate(nums):
            curr += 1 if num == 1 else -1
            if curr in count:
                ans = max(ans, i - count[curr])
            else:
                count[curr] = i
        return ans

        