# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        if root is None:
            return None

        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        
        else:
            L = self.trimBST(root.left, low, high)
            R = self.trimBST(root.right, low, high)
            root.left = L
            root.right = R
            return root
