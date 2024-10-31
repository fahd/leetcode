class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        o = dict()
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            
            if diff in o:
                return [o[diff], i]

            else:
                o[num] = i