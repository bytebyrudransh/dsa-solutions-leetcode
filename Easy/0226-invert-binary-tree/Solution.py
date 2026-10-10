# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checks(self, root : TreeNode)-> TreeNode | None:
        if root==None: 
            return None
        lt=self.checks(root.left)
        rt=self.checks(root.right)
        root.left=rt
        root.right=lt
        return root
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        return self.checks(root)
        