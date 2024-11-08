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
        