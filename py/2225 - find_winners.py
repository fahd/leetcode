'''
[1,3],
[2,3],
[3,6]
    3:2
    6:1

set_w = (
    1,
    2
)

add loser to loser hashmap

if winner is not in loser hashmap:
    add winner to winner set
if loser in winner set:
    remove loser from winner set

filter loser hashmap at end for loser_count == 1
'''
from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        set_w = set()
        map_l = defaultdict(int)

        for i in range(len(matches)):
            match = matches[i]
            [winner, loser] = match
            
            map_l[loser] += 1

            if winner not in map_l:
                set_w.add(winner)
            if loser in set_w:
                set_w.remove(loser)
        
        return [
            sorted(list(set_w)),
            sorted([x for x in map_l if map_l[x] == 1])
        ]
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

[[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]

losses = {
	1:0
	2:0
	3:2

}


'''

# 4 - Official - Even Betterer
def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses_count = [-1] * 100001

        for winner, loser in matches:
            if losses_count[winner] == -1:
                losses_count[winner] = 0
            if losses_count[loser] == -1:
                losses_count[loser] = 1
            else:
                losses_count[loser] += 1
            
        answer = [[], []]
        for i in range(100001):
            if losses_count[i] == 0:
                answer[0].append(i)
            elif losses_count[i] == 1:
                answer[1].append(i)
                
        return answer

# 3 - Official

class Solution: 
    def findWinners(self, matches: List[List[int]]) ->List[List[int]]: 
        losses_count = {}
        
        for winner, loser in matches:
            losses_count[winner] = losses_count.get(winner, 0)
            losses_count[loser] = losses_count.get(loser, 0) + 1
        
        zero_lose, one_lose = [], []
        for player, count in losses_count.items():
            if count == 0:
                zero_lose.append(player)
            if count == 1:
                one_lose.append(player)
        
        return [sorted(zero_lose), sorted(one_lose)]

# 2

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = dict()

        for i in range(len(matches)):
            [winner, loser] = matches[i]
            if winner not in losses:
                losses[winner] = losses.setdefault(winner,0)
            losses[loser] = losses.setdefault(loser,0) + 1
		
        winners_no_losses = [key for key, val in losses.items() if val == 0]
        single_losers = [key for key, val in losses.items() if val == 1]
        return [sorted(winners_no_losses), sorted(single_losers)]

# 1
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = dict()

        for i in range(len(matches)):
            [winner, loser] = matches[i]
			if winner not in losses:
				losses[winner] = losses.setdefault(winner,0)
			losses[loser] = losses.setdefault(loser,0) + 1
		
		winners_no_losses = [key for key, val in losses.items() if val == 0]
		single_losers = [key for key, val in losses.items() if val == 1]
		return [sorted(winners_no_losses, single_losers)]

