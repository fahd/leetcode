'''

Each iteration of the loop takes O ( log ⁡ n ) O(logn) time from the heap operations. The number of operations needed is linear with n. While you may be thinking: if we have a huge number, it would need to be halved many times. True, but each operation on it would also reduce the sum by a large amount. This gives us a time complexity of O ( n ⋅ log ⁡ n ) O(n⋅logn).
'''
import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        heap = [-num for num in nums]
        heapq.heapify(heap)
        
        ans = 0
        while target > 0:
            ans += 1
            x = heapq.heappop(heap)
            target += x / 2
            heapq.heappush(heap, x / 2)
        
        return ans
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
            
        
        
            

        
