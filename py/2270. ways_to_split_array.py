# [10, 4, -8, 7]
# [10, 14, 6, 13]
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        c = 0
        n = len(nums)
        s = sum(nums)
        left = 0

        for i in range(len(nums) - 1):
            left += nums[i]
            right = s - left
            if left >= right:
                c+=1
        
        return c

# 

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        prefix_sum = [nums[0]]        
        for i in range(1,n):
            prefix_sum.append(nums[i] + prefix_sum[-1])
        
        for i in range(n - 1):
            left = prefix_sum[i]
            right = prefix[-1] - left

            if left >= right:
                count += 1
        
        return count
        
