from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        
        while q:
            n = len(q)
            running_sum = 0

            for _ in range(n):
                node = q.popleft()
                running_sum += node.val
                if node.left:
                    q.append(node.left)
                    children_added += 1
                if node.right:
                    q.append(node.right)
                    children_added += 1
            
            if len(q) == 0:
                return running_sum


        
