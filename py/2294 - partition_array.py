'''
[3,6,1,2,5]
->
[1,2,3,5,6]
 ^


'''
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = 0
        min_v = nums[0]
        count = 1
        
        for i in range(1,len(nums)):
            if nums[i] > min_v + k:
                min_v = nums[i] 
                count += 1

        return count
        
# we want elements from [x, x+k]
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
