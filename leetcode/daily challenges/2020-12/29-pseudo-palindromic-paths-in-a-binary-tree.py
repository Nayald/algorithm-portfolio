# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def isPseudoPalindromic(l):
            one = set()
            for v in l:
                if v not in one:
                    one.add(v)
                else:
                    one.remove(v)
                
            return not one or (len(one) == 1 and len(l) % 2 == 1)
        
        
        result = 0
        def dfs(root, path=[]):
            nonlocal result
            if not root:
                return
            
            if not root.left and not root.right:
                result += isPseudoPalindromic(path + [root.val])
                return 
            
            dfs(root.left, path + [root.val])
            dfs(root.right, path + [root.val])
            
            
        dfs(root)
        return result