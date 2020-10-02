# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        result = 0
        def dfs(root, val):
            nonlocal result
            if not root:
                return
            
            if not (root.left or root.right):
                result += (val << 1) + root.val
                return
                
            if root.left:
                dfs(root.left, (val << 1) + root.val)
            
            if root.right:
                dfs(root.right, (val << 1) + root.val)
                
        dfs(root, 0)
        return result