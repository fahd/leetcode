# [1,2,3,4,5]
#          i
# ncurr = 9 + 5 - 2
# curr = 12
# avg = 4
def findMaxAverage(nums, k):
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
    

# print(findMaxAverage([1,2,3,4,5],3))