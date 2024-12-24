# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodes = []
        def dfs(node):
            if not node:
                return    
            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)
        dfs(root)
        return min([abs(nodes[i] - nodes[i-1]) for i in range(1,len(nodes))])
