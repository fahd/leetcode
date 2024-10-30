'''
[7,4,3,9,1,8,5,2,6]
        i
    l           r
            
li = 2
ri = 8

45 - 11
34 / 7

[7,11,14,23,24,32,37,39,45]
[-1, -1, -1, 5, 4, 4, -1, -1, -1]
'''

from typing import List

# My Solution

class Solution:
	def getAverages(self, nums: List[int], k: int) -> List[int]:
		n = len(nums)
		r = (k * 2) + 1
		avgs = []
		prefix_sum = [nums[0]]
		
		for i in range(1,len(nums)):
			prefix_sum.append(nums[i] + prefix_sum[-1])

		for i in range(len(nums)):
			l_idx = i - k
			r_idx = i + k
			
			if l_idx < 0 or r_idx >= n:
				avgs.append(-1)
			else:
				if l_idx == 0:
					avgs.append(prefix_sum[r_idx] // r)
				else:
					avgs.append((prefix_sum[r_idx] - prefix_sum[l_idx - 1]) // r)
		
		return avgs
		
# Official Solution

'''
[7,4,3,9,1,8,5,2,6]
       i
 l           r
 l = 0
 r = 6
[0,7,11,14,23,24,32,37,39,45]
                    r + 1

'''
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # When a single element is considered then its average will be the number itself only.
        if k == 0:
            return nums

        window_size = 2 * k + 1
        n = len(nums)
        averages = [-1] * n

        # Any index will not have 'k' elements in it's left and right.
        if window_size > n:
            return averages

        # Generate 'prefix' array for 'nums'.
        # 'prefix[i + 1]' will be sum of all elements of 'nums' from index '0' to 'i'.
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # We iterate only on those indices which have atleast 'k' elements in their left and right.
        # i.e. indices from 'k' to 'n - k'
        for i in range(k, n - k):
            leftBound, rightBound = i - k, i + k
            subArraySum = prefix[rightBound + 1] - prefix[leftBound]
            average = subArraySum // window_size
            averages[i] = average

        return averages
		
	