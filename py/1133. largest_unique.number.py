# 2 -> O(n) time, O(n) space
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        c = Counter(nums)

        unique_numbers = [num for num, count in c.items() if count == 1]

        return max(unique_numbers, default = -1)

# 1 -> O(n log n) time, O(1) space
def largestUniqueNumber(nums):
    l = r = 0
    nums.sort()
    curr = -1

    while l < len(nums) and r < len(nums):
        while r < len(nums) and nums[l] == nums[r]:
            r += 1
        if r - l <= 1:
            curr = nums[l]
        l = r
    return curr
        

print(largestUniqueNumber([0,0,1,0,0]))