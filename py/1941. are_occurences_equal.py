# Time and Space Complexity
# Time -> O(n)
# Space -> O(k) -> k = # unique characters
	#  Some argue this is O(1), since this is bounded by a constant

# 3
from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1

# 2
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hash_map = dict()
        for item in s:
            hash_map.setdefault(item,0)
            hash_map[item] += 1
        return len(set(hash_map.values())) == 1

# 1
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hash_map = dict()
        limit = 0
        for item in s:
            hash_map[item] = hash_map.setdefault(item,0)
            hash_map[item] += 1
            limit = max(limit, hash_map[item])
        for item in hash_map:
            count = hash_map[item]
            if count != limit:
                return False
        return True
        