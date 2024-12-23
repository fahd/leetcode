from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        a = []
        q = deque([root])

        if not root:
            return []

        while q:
            local_max = float('-inf')
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                local_max = max(node.val, local_max)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            a.append(local_max)
        return a
