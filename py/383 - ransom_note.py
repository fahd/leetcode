
'''
 O(1) Space
 O(2n) -> O(n) Time
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0] * 26
        for char in magazine:
            char_code = ord(char) - ord('a')
            arr[char_code] += 1
        for char in ransomNote:
            char_code = ord(char) - ord('a')
            arr[char_code] -= 1
            if arr[char_code] < 0:
                return False
        return True

        

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
