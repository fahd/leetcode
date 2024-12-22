class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        
        def dfs(node):
            nonlocal d
            
            if node is None:
                return 0
            
            left = 0
            right = 0

            if node.left:
                left = 1 + dfs(node.left)
            if node.right:
                right = 1 + dfs(node.right)
            
            d = max(left + right, d)
            
            return max(left, right)
            
        dfs(root)
        return d
