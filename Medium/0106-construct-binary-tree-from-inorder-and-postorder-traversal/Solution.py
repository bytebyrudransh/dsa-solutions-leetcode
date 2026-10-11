# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:


        #post order: the last element is the root

        mapping = {}

        for i in range(len(inorder)):

            mapping[inorder[i]] = i    #pair of element with index

        def build(start, end):

            if start > end:
                return None

            root = TreeNode(postorder.pop())                   #initialize root Node with last of postorder
            mid = mapping[root.val]   #get the index

            root.right = build(mid + 1, end)        #POST ORDER: LEFT -> RIGHT -> ROOT, FIND ROOT, FIND RIGHT, LEFT
            root.left = build(start, mid - 1)      

            return root



        return build(0, len(postorder) - 1)
        