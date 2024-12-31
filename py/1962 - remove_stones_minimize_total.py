from heapq import *
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        c = 0

        piles = [-pile for pile in piles]
        heapify(piles)

        for _ in range(k):
            n = -heappop(piles)
            subtractor = n // 2
            diff = n - subtractor
            heappush(piles,-diff)
            c+= 1

            s = -sum(piles)
            return s

import math
from heapq import *
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        c = 0

        piles = [-pile for pile in piles]
        heapify(piles)

        while c < k:
            n = abs(-heappop(piles))
            subtractor = math.floor(n // 2)
            diff = abs(n - subtractor)
            heappush(piles,-diff)
            c+= 1
        
        s = sum([abs(pile) for pile in piles])
        return s

