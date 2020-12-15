# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        max_depth = 0
        paths = []
        
        def dfs(root, path=[]):
            nonlocal max_depth, paths
            if not root:
                if len(path) > max_depth:
                    paths = [path]
                    max_depth = len(path)
                elif len(path) == max_depth:
                    paths.append(path)
                return
            
            dfs(root.left, path + [root])
            dfs(root.right, path + [root])
            
        
        dfs(root)
        result = root
        for i in range(1, len(paths[0])):
            if any(path[i] != paths[0][i] for path in paths[1:]):
                break
                  
            result = paths[0][i]
            
        return result