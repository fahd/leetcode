'''
[-1, 0, 3, 5, 9, 12]
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s_idx = 0
        e_idx = len(nums) - 1

        while s_idx <= e_idx:
            m = (s_idx + e_idx) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] > target:
                e_idx = m - 1
            else:
                s_idx = m + 1
        
        return -1
