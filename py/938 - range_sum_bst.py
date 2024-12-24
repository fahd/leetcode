# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, node, low, high):
        if node is None:
            return 0
        if node.val > high:
                return self.traverse(node.left, low, high)
        elif node.val < low:
                return self.traverse(node.right, low, high)
        elif node.val >= low and node.val <= high:
                return node.val + self.traverse(node.left, low, high) + self.traverse(node.right, low, high)
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.traverse(root, low, high)
