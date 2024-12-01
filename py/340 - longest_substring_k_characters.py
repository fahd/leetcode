'''

 eceba
   l
    r

 o = {
   e:1 
   b:1
 }
'''
from collections import defaultdict

def find_longest_substring(s, k):
    counts = defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans

def longest_substring(s, k):
    l = 0
    o = dict()
    n = len(s)
    c = 0
    for r in range(n):
        right = s[r]
        o[right] = o.get(right, 0) + 1
        while len(o) > k:
            left = s[l]
            o[left] -= 1
            if o[left] == 0:
                del o[left]  # Remove the character entirely if its count is 0
            l += 1
        c = max(c, r - l + 1)
    return c

print(longest_substring('eceba', 2))
