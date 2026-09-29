
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        self.res = 0
        def traverse(node):
            if not node:
                return 0

            if not node.left and not node.right:
                self.res += 1
                return node.val
            
            left = traverse(node.left)
            right = traverse(node.right)
            if node.val >= left and node.val >= right:
                self.res += 1
            return max(node.val, left, right)
        traverse(root)
        return self.res