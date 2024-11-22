class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = set(jewels)
        c = 0
        for char in stones:
            if char in dic:
                c += 1
        return c


        
