# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None :
            return None
        
        if root.left is not None :
            self.flatten(root.left)
        
        if root.right is not None :
            self.flatten(root.right)
            
        if root.left is None and root.right is not None :
            return root
        
        elif root.left is not None and root.right is None :
            root.right = root.left
            root.left = None
            return root
        
        elif root.left is not None and root.right is not None :
            last = root.left
            while last.right is not None :
                last = last.right
            last.right = root.right
            
            root.right = root.left
            root.left = None
            return root
        