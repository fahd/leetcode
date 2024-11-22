class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        o = dict()
        for char in ransomNote:
            o[char] = o.get(char, 0) + 1
        for char in magazine:
            if char in o:
                o[char] -= 1
                if o[char] == 0:
                    del o[char]
        return len(o) == 0
