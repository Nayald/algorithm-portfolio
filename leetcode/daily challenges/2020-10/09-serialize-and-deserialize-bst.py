# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        l = []
        def preOrder(root):
            if not root:
                l.append("n")
                return
            
            l.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)
        
        
        preOrder(root)
        #print(",".join(l))
        return ",".join(l)
    

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        l = list(map(lambda x: int(x) if x != "n" else None, data.split(",")))
        if not l or l[0] is None:
            return None
        
        root = TreeNode(l[0])
        nodes = []
        i = 1
        left = True
        current = root
        while i < len(l):
            val = l[i]
            i += 1
            if left:
                if val is not None:
                    #print("new left child for", current.val)
                    current.left = TreeNode(val)
                    nodes.append(current)
                    current = current.left
                else:
                    #print("left child of", current.val, "is null")
                    left = False
                
                continue
                
            if val is not None:
                #print("new right child for", current.val)
                current.right = TreeNode(val)
                current = current.right
                left = True
            else:
                if not nodes:
                    break
                current = nodes.pop()
                #print("right child of", current.val, "is null, backtrack to", current.val)
                
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans