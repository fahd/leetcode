class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = count = 0
        counts = dict({0:1})
        for i in range(len(nums)):
            num = nums[i]
            curr += num
            if curr - k in counts:
                count += counts[curr - k]
            counts.setdefault(curr, 0)
            counts[curr] += 1
        return count

 