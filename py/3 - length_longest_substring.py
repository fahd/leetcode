class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dic = dict()
        max_len = 0
        n = len(s)

        for r in range(n):
            if s[r] in dic and dic[s[r]] >= l:
                l = dic[s[r]] + 1
            dic[s[r]] = r
            print('l',l,'r',r)
            max_len=max(max_len, r - l + 1)
        return max_len

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        seen = set()
        for r in range(len(s)):
            r_char = s[r]
            l_char = s[l]
            while r_char in seen and l < r:
                seen.remove(s[l])
                l += 1

            seen.add(r_char)
            
            max_len = max(max_len, r - l + 1)
        return max_len

def length_of_longest_substring(s):
    l = r = 0
    n = len(s)
    count = dict()
    longest = 0
    for r in range(n):
        char = s[r]
        if char in count and l <= count[char] :
            l = count[char] + 1
            count[char] = l
        count[char] = r
        longest = max(longest, r - l + 1)
    return longest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        count = dict()
        longest = 0

        for r in range(n):
            char = s[r]
            # If the character is repeated, update `l` to the right of its last occurrence
            if char in count and count[char] >= l:
                l = count[char] + 1
            
            # Update the character's most recent position
            count[char] = r
            
            # Calculate the length of the current substring and update the result
            longest = max(longest, r - l + 1)
        return longest
