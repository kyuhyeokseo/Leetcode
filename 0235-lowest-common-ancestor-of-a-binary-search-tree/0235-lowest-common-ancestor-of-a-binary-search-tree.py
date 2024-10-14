# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        curr = root
        P, Q = p.val, q.val
        
        while True :
            
            #print(curr.val)
            
            if (curr.val - P) * (curr.val - Q) <= 0 :
                return curr
            else :
                if P < curr.val and Q < curr.val :
                    curr = curr.left
                elif P > curr.val and Q > curr.val :
                    curr = curr.right
        
        
        
        
        
        
        
        
        