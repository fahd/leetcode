class Solution:
    def reverseWords(self, s: str) -> str:
        l = r = 0
        n = len(s)
        a = []

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

