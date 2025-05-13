# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root is None:
            return False
        
        if self.identical(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def identical(self, root, subRoot):
        if root and subRoot:
            return root.val == subRoot.val and self.identical(root.left, subRoot.left) and self.identical(root.right, subRoot.right)
        
        return (root is None and subRoot is None)