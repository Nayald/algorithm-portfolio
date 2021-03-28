# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def helper(root, c=0):
            if not root:
                return c
            
            root.val += helper(root.right, c)
            return helper(root.left, root.val)
            
        helper(root)
        return root