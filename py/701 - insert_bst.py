
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, val):
        if not node:
            return
        if val < node.val:
            if not node.left:
                node.left = TreeNode(val)
                return
            else:
                self.traverse(node.left, val)

        elif val > node.val:
            if not node.right:
                node.right = TreeNode(val)
                return
            else:
                self.traverse(node.right, val)

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        self.traverse(root,val)
        return root
