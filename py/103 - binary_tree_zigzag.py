from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        a = []
        left_to_right = True
        if not root:
            return []
        while q:
            levels = []
            n = len(q)
            for _ in range(n):
                node =  q.popleft()
                levels.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if left_to_right:
                a.append(levels)
            else:
                a.append(levels[::-1])
            left_to_right = not left_to_right
            
        return a
