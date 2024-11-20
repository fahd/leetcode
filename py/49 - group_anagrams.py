from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            l[key].append(s)
		return l.values()
        
        