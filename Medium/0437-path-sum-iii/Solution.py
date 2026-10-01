# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Base case: sum from root equals targetSum

        def dfs(node: Optional[TreeNode], curr_sum: int) -> int:
            if not node:
                return 0

            curr_sum += node.val
            # Count paths ending at the current node
            count = prefix_sums[curr_sum - targetSum]

            # Add current prefix sum to the map for descendants
            prefix_sums[curr_sum] += 1

            # Recurse down
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            # Backtrack: remove current sum so it doesn't affect sibling branches
            prefix_sums[curr_sum] -= 1

            return count

        return dfs(root, 0)