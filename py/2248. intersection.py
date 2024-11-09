# O(n * m) -> n = length of the array, m = number of items in each list
# Official
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        d = dict()
        a = []
        n = len(nums)
        for arr in nums:
            for el in arr:
                d[el] = 0 if not el in d else d[el]                 
                d[el] += 1
                if d[el] == n:
                    a.append(el)
        a.sort()
        return a
        

# Attempt #1
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        d = dict()
        a = []
        n = len(nums)
        for arr in nums:
            for el in arr:
                d[el] = 0 if not el in d else d[el]                 
                d[el] += 1
                if d[el] == n:
                    a.append(el)
        a.sort()
        return a
        