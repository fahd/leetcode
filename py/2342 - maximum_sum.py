#
class Solution:
    def sum_digits(self, num:int):
        sum = 0
        while num > 0:
            sum += num % 10
            num = num // 10
        return sum
    def maximumSum(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        max_sum = -1

        for num in nums:
            digit_sum = self.sum_digits(num)
            if digit_sum in counter:
                max_sum = max(max_sum, num + counter[digit_sum])
            counter[digit_sum] = max(counter[digit_sum], num)
        return max_sum
#
# Solution 1
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

