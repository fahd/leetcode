

'''
[1,2,3,5]

{
    0:1
    1:1,
    3:1,
    6:1,
    11:1
}

[-1,-1,1,1,-1]
            ^
{
     0:2, -> in the case that curr - k == 0
    -1:3,
    -2:1,
}
c = 4
curr = -1

key = prefix_sum
value = number of times that prefix_sum has been seen

'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = dict({0:1})
        n = len(nums)
        curr = 0
        count = 0

        for r in range(n):
            num = nums[r]
            curr += num
            if curr - k in counts:
                count += counts[curr - k]
            counts[curr] = counts.get(curr,0) + 1
        return count


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

 
