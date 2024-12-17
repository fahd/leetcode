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

function invert(root: TreeNode | null): void {
    if (!root) return;
    invert(root.left);
    invert(root.right);
    [root.left, root.right] = [root.right, root.left];
}

function invertTree(root: TreeNode | null): TreeNode | null {
    invert(root);
    return root;
};