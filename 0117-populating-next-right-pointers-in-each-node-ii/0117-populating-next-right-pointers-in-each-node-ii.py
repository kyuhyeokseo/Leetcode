"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if root is None :
            return None
        
        tmp = [root]
        self.assign_next(tmp)
        return root
        
        
    def assign_next(self, node_list):
        L = len(node_list)
        tmp = []
        if L == 0 :
            return True
        
        if L != 0 :
            for i in range(L) :
                target = node_list[i]
                if i < L-1 :
                    target.next = node_list[i+1]
                else :
                    target.next = None
                
                if target.left is not None :
                    tmp.append(target.left)
                if target.right is not None :
                    tmp.append(target.right)
        
        self.assign_next(tmp)