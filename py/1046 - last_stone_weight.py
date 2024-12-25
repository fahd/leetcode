'''
    [1,2,4,1,7,8]
    [-8,-7,-4,2,1,1]
    pop -> 8, 7
    [-4,-2,-1,-1]
        
'''
# Solution 2:
from heapq import *
class solution:
	def laststoneweight(self, stones) -> int:
        stones = [-stone for stone in stones]
    
        heapify(stones)

        while len(stones) > 1:
            second = abs(heappop(stones))
            first = abs(heappop(stones))
            if first == second:
                heappush(stones,0) 
            else:
                new_value = -(abs(second - first))
                heappush(stones, new_value)
	    return -stones[0] if len(stones) else 0	
                
                

# Solution 1

from heapq import *
class solution:
	def createheap(self,stones, first):
		max_heap = []
		if first:
			for v in stones:
				heappush(max_heap, -v)
		else:
			for v in stones:
				heappush(max_heap, v)
		return max_heap

	def laststoneweight(self, stones) -> int:
		if not stones:
			return 0
		
		max_heap = self.createheap(stones, true)
		
		while len(max_heap) > 1:
			usecond = -heappop(max_heap)
			first = -heappop(max_heap)
			
			if second == first:
				new_stone = 0
			else:
				new_stone = second - first
			heappush(max_heap, -new_stone)
			max_heap = self.createheap(max_heap, false)
		return -max_heap.pop()
		
