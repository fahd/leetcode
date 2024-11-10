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