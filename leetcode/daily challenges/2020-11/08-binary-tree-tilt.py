# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return valtiltsum(root)[1]
    
def valtiltsum(root):
    left = right = (0, 0, 0)
    if root.left:
        left = valtiltsum(root.left)

    if root.right:
        right = valtiltsum(root.right)
        
    return root.val, left[1] + right[1] + abs(left[2] - right[2]), root.val + left[2] + right[2]
        
        
        