class Solution:
    def repeatedCharacter(self, s: str) -> str:
        o = set()
        for c in s:
            if c in o:
                return c
            o.add(c)