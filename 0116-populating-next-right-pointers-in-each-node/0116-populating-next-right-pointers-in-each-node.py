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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root is None :
            return None
        
        curr_level = [root]
        
        while len(curr_level)>0 :
            
            curr_level_tmp = []
            L = len(curr_level)
            
            #print(curr_level)
            
            for i in range(L):
                curr = curr_level[i]
                
                #print(curr.val)
                
                if i == L-1 :
                    curr.next = None
                else :
                    curr.next = curr_level[i+1]
                
                if curr.left :
                    curr_level_tmp.append(curr.left)
                if curr.right :
                    curr_level_tmp.append(curr.right)
            
            curr_level = curr_level_tmp[:]
        
        return root
            
            
                    
        
        
        
        
        
        