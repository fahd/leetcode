class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        return max(left, right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.global_max = 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, local_max):
            if not node:
                return
            self.global_max = max(self.global_max, local_max)
            dfs(node.left, local_max + 1)
            dfs(node.right, local_max + 1)

        dfs(root, self.global_max)
        return self.global_max


        
