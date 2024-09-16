# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None :
            return 0
        
        lh = self.minDepth(root.left)
        rh = self.minDepth(root.right)
        
        if lh * rh > 0 :
            return min(lh, rh) + 1
        else :
            return max(lh, rh) + 1
        