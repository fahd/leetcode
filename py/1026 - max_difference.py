class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_max, curr_min, max_diff):
            if node is None:
                return max_diff
            
            new_max = max(curr_max, node.val)
            new_min = min(curr_min, node.val)

            new_diff = max(abs(new_max - new_min), max_diff)
            
            left = dfs(node.left, new_max, new_min, new_diff)
            right = dfs(node.right, new_max, new_min, new_diff)

            return max(left,right)

        return dfs(root, root.val, root.val, float('-inf'))
        
