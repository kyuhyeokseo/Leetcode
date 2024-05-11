# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if root is None :
            return 0
        
        
        lh = self.get_lh(root)
        rh = self.get_rh(root)
        
        if lh == rh :
            return (2**rh - 1)
        
        else :
            
            return (1 + self.countNodes(root.left) + self.countNodes(root.right))
            
        
        
        
    def get_lh(self, root) :
        if root is None :
            return 0
        h = 0
        while root is not None :
            root = root.left
            h += 1
        return h
    
    def get_rh(self, root) :
        if root is None :
            return 0
        h = 0
        while root is not None :
            root = root.right
            h += 1
        return h
        