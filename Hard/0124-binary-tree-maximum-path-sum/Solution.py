class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
       res=[root.val]
       def dfs(root):
        if not root:
            return 0
        leftMax=dfs(root.left)
        rightMax=dfs(root.right)
        leftMax=max(0,leftMax)
        rightMax=max(0,rightMax)
        res[0]=max(res[0],root.val+leftMax+rightMax) 
        return root.val+max(leftMax,rightMax)
       dfs(root)
       return res[0]