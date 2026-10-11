class Solution:
	def flatten(self, n: TreeNode) -> None:
		while n:
			temp = n.left # get left tree
			if temp:
				while temp.right: # find its right most node
					temp = temp.right
				temp.right, n.right, n.left = n.right, n.left, None # "cut" n.right and attach it to temp
			n = n.right