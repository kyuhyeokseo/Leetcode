# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.valid = True
        
        if root is None :
            return None 
        
        if root.left is None and root.right is None :
            return self.valid
        
        elif root.left is None and root.right is not None :
            r_min, r_max = self._check(root.right)
            if r_min <= root.val :
                self.valid = False
            return self.valid
        
        elif root.left is not None and root.right is None :
            l_min, l_max = self._check(root.left)
            if l_max >= root.val :
                self.valid = False
            return self.valid
        
        elif root.left is not None and root.right is not None :
            l_min, l_max = self._check(root.left)
            r_min, r_max = self._check(root.right)
            if r_min <= root.val :
                self.valid = False
            if l_max >= root.val :
                self.valid = False
            return self.valid
        
        
        
    def _check(self, root) :
        
        if root.left is None and root.right is None :
            return root.val, root.val
        elif root.left is None and root.right is not None :
            r_min, r_max = self._check(root.right)
            if r_min <= root.val :
                self.valid = False
            return root.val, r_max
        elif root.left is not None and root.right is None :
            l_min, l_max = self._check(root.left)
            if l_max >= root.val :
                self.valid = False
            return l_min, root.val
        elif root.left is not None and root.right is not None :
            l_min, l_max = self._check(root.left)
            r_min, r_max = self._check(root.right)
            if r_min <= root.val :
                self.valid = False
            if l_max >= root.val :
                self.valid = False
            return l_min, r_max
            
        
        