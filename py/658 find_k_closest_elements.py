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
        
        
        
