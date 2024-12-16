class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) < 2:
            return s
        stack = []
        for c in s:
            if stack:
                last = stack[-1]
                if last.islower() and c == last.upper():
                    stack.pop()
                elif last.isupper() and c == last.lower():
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return "".join(stack)
