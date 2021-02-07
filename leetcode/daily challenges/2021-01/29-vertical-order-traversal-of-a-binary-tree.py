# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = defaultdict(list)
        
        def dfs(root, x, y):
            if not root:
                return
            
            d[x].append((y, root.val))
            if root.left:
                dfs(root.left, x-1, y+1)
            if root.right:
                dfs(root.right, x+1, y+1)
            
        dfs(root, 0, 0)
        #print(d)
        r = [None] * len(d)
        offset = min(d.keys())
        for k, v in d.items():
            r[k - offset] = [x[1] for x in sorted(v)] 
        
        return r 
        
        