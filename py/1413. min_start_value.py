class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        mV = nums[0]
        for i in range(1, len(nums)):
            nV = nums[i] + prefix_sum[-1]
            mV = min(mV, nV)
            prefix_sum.append(nV)
        if mV < 0:
            return abs(mV) + 1
        else:
            return 1