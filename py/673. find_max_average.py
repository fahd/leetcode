def findMaxAverage(self, nums: List[int], k: int) -> float:
        t = 0
        curr = 0
        avg = 0
        for i in range(k):
            curr += nums[i]
        avg = curr / k
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            avg = max(avg, curr / k)
        return avg
        