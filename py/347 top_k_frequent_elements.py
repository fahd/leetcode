class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums) # O(n) time, O(n) space
        l = list(map.items()) #O(n) time, O(n) space
        l.sort(key = lambda x:x[1], reverse=True) # O(n log n) time
        o = [k for k,v in l[0:k]] #O(k) time, O(k) space
        return o 
        # total time complexity, O(n) time, O(n) space
