class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, prev_val):
            if not node:
                return 0
            elif node.val >= prev_val:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            else:
                return dfs(node.left, prev_val) + dfs(node.right, prev_val)

        return dfs(root, root.val)