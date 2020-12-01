# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache

class Solution:
    def rob(self, root: TreeNode) -> int:        
        @lru_cache
        def helper(root, skip=True):
            if not root:
                return 0
            
            sleft = helper(root.left.left) + helper(root.left.right) if root.left else 0
            sright = helper(root.right.left) + helper(root.right.right) if root.right else 0
            
            return max(root.val + sleft + sright, helper(root.left) + helper(root.right))
        
        
        return helper(root)