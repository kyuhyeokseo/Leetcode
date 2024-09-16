# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        _, flag = self.getHeight(root)

        return flag
        
    def getHeight(self, root):
        
        if root is None :
            return 0, True
        
        else :
            lh, lb = self.getHeight(root.left)
            rh, rb = self.getHeight(root.right)
            
            if lb and rb :
                return max(lh, rh) + 1, abs(lh-rh) < 2
            else :
                return -1, False
            