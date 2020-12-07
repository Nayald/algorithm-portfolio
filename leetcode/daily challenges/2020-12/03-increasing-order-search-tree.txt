# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        head = TreeNode(None)
        right = head
        curr = root
        while True:
            while curr.left:
                stack.append(curr)
                curr = curr.left
                stack[-1].left = None
                
            right.right = curr
            right = curr            
                            
            if curr.right:
                curr = curr.right
                continue
                
            if not stack:
                break
                
            curr.right = stack.pop()
            curr = curr.right
            
        return head.right

	#inorder = []
        #def helper(root):
        #    if not root:
        #        return
        #    
        #    helper(root.left)
        #    inorder.append(root)
        #    helper(root.right)
        #    
        #
        #helper(root)
        #head = TreeNode(None)
        #curr = head
        #for n in inorder:
        #    n.left = None
        #    curr.right = n
        #    curr = n
        #    
        #return head.right