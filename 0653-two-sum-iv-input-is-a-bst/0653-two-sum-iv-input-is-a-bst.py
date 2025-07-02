# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        self.K = k
        self.D = {}
    
        return self.find(root)


    def find(self, root):

        if root is None:
            return False
        
        if root.val in self.D:
            return True
        else:
            self.D[self.K-root.val] = True
        
        return self.find(root.left) or self.find(root.right)
