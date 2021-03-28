# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def helper(root):            
            if not root:
                return None
            
            if root.val > high:
                return helper(root.left)
            elif root.val < low:
                return helper(root.right)
                
            root.left = helper(root.left)
            root.right = helper(root.right)
                
            return root
        
        
        return helper(root)