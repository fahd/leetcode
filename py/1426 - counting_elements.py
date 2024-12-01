class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = set(arr)
        count = 0
        for num in arr:
            if num + 1 in counter:
                count += 1
        return count
        



# O(n log n) time O(1) space
class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()
        l = 0
        r = 1
        n = len(arr)
        count = 0

        while l < n and r < n:
            num_left = arr[l]
            num_right = arr[r]

            if num_right - num_left == 0:
                r += 1
            elif num_right - num_left > 1:
                l += 1
            else:
                count += 1
                l += 1
        return count
