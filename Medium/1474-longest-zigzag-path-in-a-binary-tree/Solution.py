class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, step, goLeft, maxPath):
            if not root:
                return None

            maxPath[0] = max(maxPath[0], step)
        
            if goLeft:
                dfs(root.left, step + 1, False, maxPath)
                dfs(root.right, 1, True, maxPath)
            else:
                dfs(root.left, 1, False, maxPath)
                dfs(root.right, step + 1, True, maxPath)
    
        maxPath = [0]
        dfs(root, 0, True, maxPath)

        return maxPath[0]