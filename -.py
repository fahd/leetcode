from heapq import *
class Solution:
	def createheap(self,stones, first):
		max_heap = []
		if first:
			for v in stones:
				heappush(max_heap, -v)
		else:
			for v in stones:
				heappush(max_heap, v)
		return max_heap

	def lastStoneWeight(self, stones) -> int:
		if not stones:
			return 0
		
		max_heap = self.createheap(stones, True)
		
		while len(max_heap) > 1:
			second = -heappop(max_heap)
			first = -heappop(max_heap)
			
			if second == first:
				new_stone = 0
			else:
				new_stone = second - first
			heappush(max_heap, -new_stone)
			max_heap = self.createheap(max_heap, False)
		return max_heap.pop()
		
		

			


		

heap = Solution()
print(heap.lastStoneWeight([8,1,10,19]))
'''
19, 10, 8, 1
->
9, 8, 1
->

->
8, 1, 1
'''