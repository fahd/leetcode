# Attempt 2
class Solution:
    def reverseWords(self, s: str) -> str:
        l = r = 0
        n = len(s)
        a  = list(s)

        for r in range(n + 1):
            if r == n or s[r] == ' ':
                self.reverse(a, l, r - 1)
                l = r + 1
        return "".join(a)
            
    def reverse(self, a:str, l:int, r:int):
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1

# Attempt 1
class Solution:
    def reverseWords(self, s: str) -> str:
        l = r = 0
        n = len(s)
        a = list(s)

        while r <= n:
            if r < n and s[r] != ' ':
                r += 1
                continue
            l = r
            if l==n or s[l] == ' ':
                l -= 1
            while l >= 0 and s[l] != ' ':
                a.append(s[l])
                l -= 1
            if r < n and s[r] == ' ':
                a.append(' ')
            r += 1
        
        return "".join(a)

