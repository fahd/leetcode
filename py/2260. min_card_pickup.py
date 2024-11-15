from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = float('inf')
        l = defaultdict(list)

        for i,card in enumerate(cards):
            l[card].append(i)
        
        for key in l:
            arr = l[key]
            for i in range(len(arr)-1):
                ans = min(ans, arr[i+1] - arr[i] + 1)
            
        return -1 if ans == float('inf') else ans