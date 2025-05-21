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

    def preorder(self, root: 'Node') -> List[int]:
        
        self.preorder_save(root)
        return self.ret

    def preorder_save(self, root):
        if root is None:
            return True
        
        self.ret.append(root.val)
        if root.children:
            for c in root.children:
                self.preorder_save(c)
        
        return True