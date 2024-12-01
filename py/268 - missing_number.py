#4
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ''' Only needs to be length of numbers because we start with 1, the problem starts with a 0 as the first index
        '''
        n = len(nums)
        # s_hypothetical = sum([x for x in range(n)])
        
        '''Even better, sum of first n numbers'''
        s_hypothetical = n * (n+1) // 2
        s_actual = sum(nums)

        return s_hypothetical - s_actual
        
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
