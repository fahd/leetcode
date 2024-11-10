'''
winners = {
    1:1
    2:1
    10:2
}

losers = {
    3:2
    4:1
    5:1
    6:2
    7:1
    8:1
    9:2
}

winners = [1,2,10]
losers = [4,5,7,8]


'''
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = []
        w = set()
        l = dict()

        losers = []

        for i in range(len(matches)):
            match = matches[i]
            [winner, loser] = match
            
            w.add(winner)
            
            l.setdefault(loser,0)
            l[loser] += 1
            
            if loser in w:
                w.remove(loser)
            if winner in l:
                w.remove(winner)
                
        for key, val in l.items():
            if val == 1:
                losers.append(key)
        
        winners = set(w)
        ans.append(sorted(winners))
        ans.append(sorted(losers))
        return ans