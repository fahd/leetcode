'''
3,2,3,1,1,1
          ^
c = 0
candidate = 1
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        c = 0

        for i in range(len(nums)):
            num = nums[i]
            if c == 0:
                candidate = num
            c += 1 if candidate == num else -1
        return candidate
            
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        c = 1
        c_max = 1
        maj = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                maj = nums[i-1] if c > c_max else maj
                c_max = max(c,c_max)
                c = 1
            c += 1
            maj = nums[i] if c > c_max else maj
        return maj
