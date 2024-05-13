# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if root is None :
            return None
        
        order = self.let_sort(root)
        return order[k-1]
        
        
    def let_sort(self, root):
        
        if root.left is None and root.right is None :
            return [root.val]
        elif root.left is None and root.right is not None :
            r = self.let_sort(root.right)
            return ([root.val] + r)
        elif root.left is not None and root.right is None :
            l = self.let_sort(root.left)
            return (l + [root.val])
        elif root.left is not None and root.right is not None :
            r = self.let_sort(root.right)
            l = self.let_sort(root.left)
            return (l + [root.val] + r)
        
        
        
        
        