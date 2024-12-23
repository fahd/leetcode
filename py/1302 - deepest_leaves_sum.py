# Solution 2
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([(root,0)])
        depth = deep_sum = 0
        
        while q:
            node, curr_depth = q.popleft()

            # When we are at a leaf
            if not node.left and not node.right:
                # if we are at the deepest node so far, set our deep_sum to the current node's value. 
                # we will add to that deep_sum by iterating over the rest of the values at that level
                if curr_depth > depth:
                    deep_sum = node.val
                    depth = curr_depth

                # when we are at either the only node at that respective level, or we are iterating over the
                # the remaining nodes at the current deepest level
                elif curr_depth == depth:
                    deep_sum += node.val
            else:
                if node.left:
                    q.append((node.left, curr_depth + 1))
                if node.right:
                    q.append((node.right, curr_depth + 1))
        return deep_sum

# Solution 1
from collections import deque class Solution:
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
                if node.right:
                    q.append(node.right)
            
            if len(q) == 0:
                return running_sum


        
