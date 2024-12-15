class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            '[':']',
            '{':'}',
            '(':')'
        }
        
        stack = []

        for c in s:
            if c in chars:
                stack.append(c)
            elif stack and chars[stack[-1]] == c:
                stack.pop()
            else:
                return False
        
        return not stack
