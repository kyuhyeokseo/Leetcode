# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        S = 0
        
        if root is None :
            return S

        cL = [root]
        
        while cL :
            
            fL = []
            for c in cL :
                if c.left :
                    fL.append(c.left)
                    if c.left.left is None and c.left.right is None :
                        S += c.left.val
                if c.right :
                    fL.append(c.right)
            cL = fL[:]
        
        return S
        
        
        
        
        
        
        
        
        
        