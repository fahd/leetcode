# 2
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        return min(c['b'], c['a'], c['l'] // 2, c['o'] // 2, c['n'])

# 1
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = 0
        c = Counter(text)

        while ( 
            'b' in c and
            'a' in c and
            'l' in c and
            'o' in c and
            'n' in c
        ):
            if c['b'] < 1 or c['a'] < 1 or c['l'] < 2 or c['o'] < 2 or c['n'] < 1:
                    break
            c['b'] -= 1
            c['a'] -= 1
            c['l'] -= 2
            c['o'] -= 2
            c['n'] -= 1
            ans += 1
        return ans