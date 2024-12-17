class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        a = [0] * len(temperatures)

        for i,t in enumerate(temperatures):
            if stack:
                while stack and t > stack[-1][1]:
                    a[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
            stack.append([i,t])
        return a
