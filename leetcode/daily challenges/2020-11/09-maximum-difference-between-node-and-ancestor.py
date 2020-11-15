# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def helper(root, vmin=10e6, vmax=-10e6):
            if not root:
                return vmax - vmin
            
            return max(helper(root.left, min(root.val, vmin), max(root.val, vmax)), helper(root.right, min(root.val, vmin), max(root.val, vmax)))
        
        return helper(root)