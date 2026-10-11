from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        res = []
        while q:
            total, count = 0, 0
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node:
                    total += node.val
                    count += 1
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(total / count)
        return res
                