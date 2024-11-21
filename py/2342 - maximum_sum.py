class Solution:
    def sumDigits(self, num:int) -> int:
        n = 0
        nc = num
        while nc != 0:
            n += nc % 10
            nc = nc // 10
        return n
    
    def maximumSum(self, nums: List[int]) -> int:
        o = defaultdict(int)
        ans = -1
        for num in nums:
            key = self.sumDigits(num)
            if key in o:
                ans = max(ans, num + o[key])
            o[key] = max(o[key], num)

        return ans

