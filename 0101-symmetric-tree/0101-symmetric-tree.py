# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if root is None :
            return True
        
        self.make_symmetric(root.left)
        
        return self.is_same(root.left, root.right)
        
        
    def make_symmetric(self, root) :
        
        if root is None :
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.make_symmetric(root.left)
        self.make_symmetric(root.right)
        
        
    def is_same(self, left, right) :
        
        if left is None and right is None :
            return True
        
        elif left is not None and right is not None :
            return (left.val == right.val) and self.is_same(left.left, right.left) and self.is_same(left.right, right.right)
        
        return False
        
        