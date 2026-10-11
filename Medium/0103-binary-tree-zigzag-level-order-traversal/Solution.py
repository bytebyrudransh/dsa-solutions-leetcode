class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def helper(root, level):
            if root:
                if len(ans) <= level:
                    ans.append([root.val])
                else:
                    ans[level].append(root.val)

                helper(root.left, level + 1)
                helper(root.right, level + 1)

        helper(root, 0)

        for i in range(1, len(ans), 2):
            ans[i] = ans[i][::-1]

        return ans