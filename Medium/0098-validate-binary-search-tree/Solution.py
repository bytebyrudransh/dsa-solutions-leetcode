# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def solve(node, leftLimit=float('-inf'), rightLimit=float('inf')):

            l = True
            r = True
            s = False

            # Check the node's value with its left child, if it exists
            if node.left:
                if node.left.val < node.val:
                    l = solve(node.left, leftLimit, node.val)
                else:
                    l = False

            # Check the node's value with its right child, if it exists
            if node.right:
                if node.val < node.right.val:
                    r = solve(node.right, node.val, rightLimit)
                else:
                    r = False

            # Check whether the node lies within its valid range
            if leftLimit < node.val < rightLimit:
                s = True
            else:
                s = False

            # All conditions must be satisfied
            if l and r and s:
                return True
            else:
                return False

        return solve(root)