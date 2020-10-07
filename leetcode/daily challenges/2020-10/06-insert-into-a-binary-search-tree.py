# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        current = root
        while current:
            if val == current.val:
                break
            
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)
                    break
                else:
                    current = current.left
                    continue
            else:
                if not current.right:
                    current.right = TreeNode(val)
                    break
                else:
                    current = current.right
                    continue
                    
        return root