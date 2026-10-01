class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node=root
        while(node):
            if node.val==val:
                return node
            if node.val<val:
                node=node.right
            else:
                node=node.left
        return None