# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lst=[]

        q=deque([root])
        while q:
            node=q.popleft()
            lst.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        lst.sort()
        mi=float('inf')
        for i in range(1,len(lst)):
            a=abs(lst[i-1]-lst[i])
            mi=min(a,mi)
        return mi    