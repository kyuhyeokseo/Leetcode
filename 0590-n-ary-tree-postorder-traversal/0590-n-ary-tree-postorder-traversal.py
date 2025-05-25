"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.ret = []

    def postorder(self, root: 'Node') -> List[int]:
        
        self.savePostOrder(root)

        return self.ret

    def savePostOrder(self, root):

        if root is None:
            return True
        
        if root.children:
            for c in root.children:
                self.savePostOrder(c)
                
        self.ret.append(root.val)

        return True