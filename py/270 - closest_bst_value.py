class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_v = float('inf')
        min_node = float('inf')
        
        def dfs(node):
            nonlocal min_v
            nonlocal min_node

            if not node:
                return
            
            loc_v = abs(node.val - target)
            # two values the same, choose the smaller node
            if loc_v == min_v:
                min_node = min(min_node, node.val)
            # when we have a new min, it's the current node
            elif loc_v < min_v:
                min_node = node.val
                min_v = loc_v
            # go left
            if target < node.val:
                dfs(node.left)
            # go right
            if target > node.val:
                dfs(node.right)
        
        dfs(root)
        
        return min_node
