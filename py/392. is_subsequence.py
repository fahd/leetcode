class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sc = 0
        i = 0

        while i < len(t):
            if sc == len(s):
                return True
            if s[sc] == t[i]:
                sc += 1
            i += 1
        
        return sc == len(s)