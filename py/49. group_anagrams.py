class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hash_map = dict()
        '''
        {
            aet: [eat, tea, ate],
            ant: [tan, nat],
            abt: [bat]
        }
        '''
        for s in strs:
            sorted_s = "".join(sorted(s))
            hash_map[sorted_s] = hash_map.get(sorted_s,[])
            hash_map[sorted_s].append(s)
        for a in hash_map.values():
            ans.append(a)
        return ans
        