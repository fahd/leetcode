# Solution 3

from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = defaultdict(list)
        for i in range(len(cards)):
            dic[cards[i]].append(i)
            
        ans = float("inf")
        for key in dic:
            arr = dic[key]
            for i in range(len(arr) - 1):
                ans = min(ans, arr[i + 1] - arr[i] + 1)
        
        return ans if ans < float("inf") else -1

# Solution 2
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_num = float("inf")

        repeats = dict()
        for i, card in enumerate(cards):
            if card in repeats:
                min_num = min(min_num, i - repeats[card] + 1)
            repeats[card] = i

        return -1 if min_num == float("inf") else min_num


# Solution 1
from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = float('inf')
        l = defaultdict(list)

        for i,card in enumerate(cards):
            l[card].append(i)
            if len(l[card]) > 1:
                ans=min(ans, l[card][-1] - l[card][-2] + 1)

        return -1 if ans == float('inf') else ans
