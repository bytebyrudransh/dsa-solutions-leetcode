class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums, level = [], [root]
        while level:
            sums.append(sum(n.val for n in level))
            level = [c for n in level for c in (n.left, n.right) if c]
        return sums.index(max(sums)) + 1