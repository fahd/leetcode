from heapq import *
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        total_cost = 0
        heapify(sticks)

        while len(sticks) > 1:
            second = heappop(sticks)
            first = heappop(sticks)
            new_stick = first + second
            total_cost += new_stick
            heappush(sticks, new_stick)
        
        return total_cost
