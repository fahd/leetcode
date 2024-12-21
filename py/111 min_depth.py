class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            if not node.left and not node.right:
                return 1
            
            left = 0
            right = 0

            if node.left:
                left = 1 + dfs(node.left)

            if node.right:
                right = 1 + dfs(node.right)
            
            if left and right:
                return min(left,right)
            elif left:
                return left
            else:
                return right

        return dfs(root)
