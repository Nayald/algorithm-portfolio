# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root, minnode=TreeNode(float("-inf")), maxnode=TreeNode(float("inf"))):
            if not root:
                return True
            
            if not minnode.val < root.val:
                minnode.val, root.val = root.val, minnode.val
                return False
            
            if not root.val < maxnode.val:
                root.val, maxnode.val = maxnode.val, root.val
                return False
                
            return dfs(root.left, minnode, root) and dfs(root.right, root, maxnode)
            
            
        while not dfs(root):
            pass