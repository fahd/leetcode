# Solution 2
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()
        for i in range(len(nums)):
            # maintain monotonic decreasing.
            # all elements in the deque smaller than the current one
            # have no chance of being the maximum, so get rid of them
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            # queue[0] is the index of the maximum element.
            # if queue[0] + k == i, then it is outside the window
            if queue[0] + k == i:
                queue.popleft()
            
            # only add to the answer once our window has reached size k
            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans


# Solution 1
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        a = []
        left, right = 0,0
        
        for i in range(len(nums)):
            # case out of bounds
            if q and (i - k + 1) > q[0]:
                q.popleft()
            # case current item is greater than the last item
            while len(q) and nums[i] > nums[q[-1]]:
                q.pop()
            
            q.append(i)

            if right - left + 1 == k:
                a.append(nums[q[0]])
                left += 1
            
            right += 1
        return a
            
        




        
