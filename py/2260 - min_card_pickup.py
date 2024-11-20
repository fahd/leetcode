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