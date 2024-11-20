class Solution:
    def sumDigits(self, num:int) -> int:
        n = 0
        nc = num
        while nc != 0:
            n += nc % 10
            nc = nc // 10
        return n

    def maximumSum(self, nums: List[int]) -> int:
        o = dict()
        ans = 0

        for num in nums:
            key = self.sumDigits(num)
            if key in o:
                mv = o[key]
                ans = max(ans, num + mv)
            o[key] = o.get(key, 0)
            o[key] = max(o[key], num)

        return -1 if ans == 0 else ans


