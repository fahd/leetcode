from heapq import *
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for n in arr:
            diff = abs(n - x)
            heappush(heap, (-diff, -n))
            if len(heap) > k:
                heappop(heap)

        return sorted([-v[-1] for v in heap])


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []
        res = []
        for n in arr:
            diff = abs(x - n)
            heapq.heappush(min_heap, (diff,n))
        
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])
        
        return sorted(res)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []
        map = defaultdict(list)
        
        for n in arr:
            diff = abs(x - n)
            map[n].append(diff)
        
        for key,val in map.items():
            c = 0 
            v = val[0]
            while c < len(val):
                heapq.heappush(min_heap, (v, key))
                c += 1        
        
        l = []
        
        for _ in range(k):
            l.append(heapq.heappop(min_heap)[1])
        
        l.sort()
        return l
        
        
        
