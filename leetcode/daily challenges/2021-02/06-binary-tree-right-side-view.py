# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        result = []
        l = [root]
        while l:
            new_l = []
            for n in l:
                if n.left:
                    new_l.append(n.left)
                if n.right:
                    new_l.append(n.right)
                
            result.append(l[-1].val)
            l = new_l
            
        return result