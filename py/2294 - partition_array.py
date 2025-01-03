class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        mn = 0
        nums.sort()
        l = 0
        for r in range(1,len(nums)):
            if nums[r] - nums[l] > k:
                l = r
                mn += 1
        return mn + 1
