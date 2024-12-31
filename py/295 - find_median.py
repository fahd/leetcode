from heapq import *
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        
        heappush(self.max_heap, -num)
        max_top = -heappop(self.max_heap)
        heappush(self.min_heap, max_top)
    
        if (len(self.min_heap) - len(self.max_heap)) > 1:
            heappush(self.max_heap, -heappop(self.min_heap))
        
    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -self.max_heap[0]
