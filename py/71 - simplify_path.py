# Solution 2
class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split("/")
        stack = []
        for p in split_path:
            if len(p) == 0 or p == '.':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)

# Solution 1
class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        if n == 1:
            return path
        stack = []
        i = 0

        while i < n:
            if path[i] == '/':
                j = i + 1
                temp = ''
                while j < n and path[j] == '/':
                    i += 1
                    j += 1
                while j < n and path[j] != '/':
                    temp += path[j]
                    j += 1
                if stack and temp == '..':
                    stack.pop()
                    stack.pop()
                elif len(temp) and temp != '..' and temp != '.':
                    stack.append("/")
                    stack.append(temp)
                
                i = j
            else:
                i += 1
        
        if not len(stack):
            return "/"
        else:
            return "".join(stack)
