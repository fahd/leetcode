class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        jewels_in_stones = [i in jewel_set for i in stones]
        return sum(jewels_in_stones)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        arr = [0] * 58
        c = 0
        
        for char in jewels:
            char_code = ord(char) - ord('a') + 32
            arr[char_code] += 1
        
        for char in stones:
            char_code = ord(char) - ord('a') + 32
            if arr[char_code] > 0:
                c += 1

        return c
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = set(jewels)
        c = 0
        for char in stones:
            if char in dic:
                c += 1
        return c


        
