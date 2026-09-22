class Solution:
    def leaf(self, root: Optional[TreeNode]) -> list(int):
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        return self.leaf(root.left) + self.leaf(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.leaf(root1) == self.leaf(root2)