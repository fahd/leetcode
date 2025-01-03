'''
[4,5,6]

'''
from heapq import *
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.max_limit = k
        
        for n in nums:
            heappush(self.min_heap, n)
            if len(self.min_heap) > k:
                heappop(self.min_heap)
        
    def add(self, val: int) -> int:
        heappush(self.min_heap, val)
        if len(self.min_heap) > self.max_limit:
            heappop(self.min_heap)
        return self.min_heap[0]
