from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = []
        queue = deque([root])

        while queue:
            stack.append(queue[-1].val)
            n = len(queue)
            for i in range(n):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                    
        return stack

# Official Solution
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = []
        queue = deque([root])

        while len(queue):
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i == n - 1:
                    stack.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                    
        return stack

# Solution 1
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root.val]
        queue = deque([{"node":root,"level":0}])
        seen = set({0})

        while len(queue):
            n = len(queue)
            for _ in range(n):
                el = queue.pop()
                
                node,level = el['node'], el['level']

                if level not in seen:
                    stack.append(node.val)
                    seen.add(level)

                if node.left:
                    queue.append({"node":node.left, "level": level + 1})

                if node.right:
                    queue.append({"node":node.right, "level": level + 1})
                    
        return stack



        
