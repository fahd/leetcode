class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        l = r = total = 0
        curr = 1

        
        while r < len(nums):
            curr *= nums[r]

            while curr >= k:
                curr /= nums[l]
                l += 1
            
            
                total += (r - l + 1)
            
            r += 1
        return total
        