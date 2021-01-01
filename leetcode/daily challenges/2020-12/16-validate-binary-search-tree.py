# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, min_val, max_val = stack.pop()
            if not node:
                continue
                
            if min_val >= node.val or node.val >= max_val:
                return False
            
            stack.append((node.left, min_val, node.val))
            stack.append((node.right, node.val, max_val))
                
        return True
        