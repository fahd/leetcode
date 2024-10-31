class Solution:
    def repeatedCharacter(self, s: str) -> str:
        o = set()
        for i in range(len(s)):
            if s[i] in o:
                return s[i]
            else:
                o.add(s[i])