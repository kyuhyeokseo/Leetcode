# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.MAX = 1000000
        
        if root is None :
            return None
        
        l_diff, l_min, l_max = self.get_all(root.left)
        r_diff, r_min, r_max = self.get_all(root.right)
        if root.left is None and root.right is not None :
            return min(r_diff, r_min-root.val)
        elif root.left is not None and root.right is None :
            return min(l_diff, root.val - l_max)
        elif root.left is not None and root.right is not None :
            return min(l_diff, r_diff, root.val - l_max, r_min - root.val)
            
        
    def get_all(self, root) :
        if root is None :
            return None, None, None
        else :
            l_diff, l_min, l_max = self.get_all(root.left)
            r_diff, r_min, r_max = self.get_all(root.right)
            if root.left is None and root.right is None :
                return self.MAX, root.val, root.val
            elif root.left is None and root.right is not None :
                return min(r_diff, r_min-root.val), root.val, r_max
            elif root.left is not None and root.right is None :
                return min(l_diff, root.val - l_max), l_min, root.val
            elif root.left is not None and root.right is not None :
                return min(l_diff, r_diff, root.val - l_max, r_min - root.val), l_min, r_max
        