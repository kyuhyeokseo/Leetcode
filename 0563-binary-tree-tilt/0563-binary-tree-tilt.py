# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tilt = 0

    def findTilt(self, root: Optional[TreeNode]) -> int:

        self.findSum(root)

        return self.tilt
        
    
    def findSum(self, root):
        
        if root is None:
            return 0
        
        LSum = self.findSum(root.left)
        RSum = self.findSum(root.right)
        self.tilt += abs(LSum - RSum)
        
        return (LSum + RSum + root.val)