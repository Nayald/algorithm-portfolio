# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root):
        self.checkpoints = []
        self.node = root
        
        
    def next(self) -> int:
        if self.node:
            while self.node.left:
                self.checkpoints.append(self.node)
                self.node = self.node.left
            
            node = self.node
            self.node = node.right
            return node.val
        elif self.checkpoints:
            node = self.checkpoints.pop()
            self.node = node.right
            return node.val
            
            
    def hasNext(self) -> bool:
        return self.node or self.checkpoints


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()