# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root, height=0):
            if not root:
                return height, True
            
            left = dfs(root.left, height + 1)
            right = dfs(root.right, height + 1)
            
            return max(left[0], right[0]), left[1] and right[1] and abs(left[0] - right[0]) <= 1
        
        return dfs(root)[1]
                
                    
            