# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

import math
class Solution:
    def firstBadVersion(self, n: int) -> int:
        s = 0
        e = n
        found = False

        while s <= e:
            m = (s + e) // 2
            if isBadVersion(m):
                e = m - 1
            else:
                s = m + 1

        return s
