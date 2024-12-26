'''
[5, 19, 8, 1]

sum = 33

1. Max Heap
2. While loop
    - Have a a new sum equal to the old sum
    - Halve the largest number (top of heap)    
    - reduce sum by half of the largest number
    - Increment number of steps
    - Compare new sum to old sum
    - add new number to heap
'''
from heapq import *
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        s = sum(nums)
        
        ns = s
        steps = 0
        nums = [-num for num in nums]
        heapify(nums)

        while len(nums):
            max_value_halved = -heappop(nums) / 2
            ns -= max_value_halved
            steps += 1
            if ns <= s / 2: 
                return steps
            heappush(nums, -max_value_halved)
            
        
        
            

        
