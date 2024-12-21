class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if not tree1 and tree2 or not tree2 and tree1:
                return False
            if tree1.val != tree2.val:
                return False
                
            return dfs(tree1.left, tree2.left) and dfs(tree1.right, tree2.right)
            
            
        return dfs(p,q)
