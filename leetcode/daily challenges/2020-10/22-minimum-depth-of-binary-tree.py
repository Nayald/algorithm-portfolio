# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        min_depth = 1
        row = [root]
        while row:
            next_row = []
            for node in row:
                if not (node.left or node.right):
                    return min_depth 
                
                if node.left:
                    next_row.append(node.left)
                
                if node.right:
                    next_row.append(node.right)
                    
            row = next_row
            min_depth += 1
            
            