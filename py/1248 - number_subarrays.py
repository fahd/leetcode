# problem type => subarrays
# constraint metric => k odd numbers

'''
   [1,1,2,1,1]
1. [1,1,2,1]
2.   [1,2,1,1]

{
    curr: count
    key = curr - k
    0:1
    1:1
    2:1
    3:1
    4:1
}

'''

from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        l = 0
        curr = 0
        count = 0
        for r in range(len(nums)):
            num = nums[r]
            curr += num % 2
            count += counts[curr - k]
            counts[curr] += 1
        return count
            
# Solutions that require sequences of elements to meet criteria often utilize prefix sums,

# Sequence of odd numbers where the amount is equal to k

# If a problem asks for the: 
	# Number of subarrays
	# Finding subarrays that meet a certain sum or count condition) (like having a specific sum, product, or a certain number of odd/even elements), it’s a good hint that the prefix sum approach could be useful.
  
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        c = a = 0
        s = dict({0:1})
        for num in nums:
            if num % 2 != 0:
                c += 1
            if c - k in s:
                a += s[c - k]
            s.setdefault(c, 0)
            s[c] += 1
        return a

