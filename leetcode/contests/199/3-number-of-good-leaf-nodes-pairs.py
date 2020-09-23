# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.d = {}
        self.dfs(root, path={root})
        
        
        r = 0
        l = list(self.d.items())
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if len(l[i][1] | l[j][1]) - len(l[i][1] & l[j][1]) <= distance:
                    r += 1
                    
        return r
    
        
    def dfs(self, root, path=set()):
        if not root:
            return
                
        if not (root.left or root.right):
            self.d[root] = path
            return
        
        if root.left:
            self.dfs(root.left, path | {root.left})
            
        if root.right:
            self.dfs(root.right, path | {root.right})