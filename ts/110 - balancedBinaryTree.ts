/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function findNodeDepth(root: TreeNode | null): number {
  if (!root) return 0;

  const lh = findNodeDepth(root.left)
  const rh = findNodeDepth(root.right)

  if (lh < 0 || rh < 0) {
      return -1
  }

  if (Math.abs(lh - rh) > 1){
      return -1
  }

  return 1 + Math.max(lh, rh);
}

function isBalanced(root: TreeNode | null): boolean {
  return findNodeDepth(root) > -1
};