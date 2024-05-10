# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if root is None :
            return None
        
        if root.right is not None :
            r_pathsum, r_sum = self.calculate_pathsum(root.right)
            
        if root.left is not None :
            l_pathsum, l_sum = self.calculate_pathsum(root.left)
        
        if root.right is None and root.left is None :
            return root.val
        
        elif root.left is None and root.right is not None :
            return max(r_pathsum, r_sum + root.val, root.val)
        
        elif root.left is not None and root.right is None :
            return max(l_pathsum, l_sum + root.val, root.val)
        
        elif root.left is not None and root.right is not None :
            return max(r_pathsum, l_pathsum, root.val, root.val+r_sum, root.val+l_sum, r_sum + root.val + l_sum)
        
        
    def calculate_pathsum(self, root) :
        
        if root.right is not None :
            r_pathsum, r_sum = self.calculate_pathsum(root.right)
            print('------ right -------')
            print(root.val, r_pathsum, r_sum)
            
        if root.left is not None :
            l_pathsum, l_sum = self.calculate_pathsum(root.left)
            print('------ left  -------')
            print(root.val, l_pathsum, l_sum)
        
        if root.right is None and root.left is None :
            return root.val, root.val
        
        elif root.left is None and root.right is not None :
            path_sum = max(r_pathsum, r_sum + root.val, root.val)
            return path_sum, max(r_sum + root.val, root.val)
        
        elif root.left is not None and root.right is None :
            path_sum = max(l_pathsum, l_sum + root.val, root.val)
            return path_sum, max(l_sum + root.val, root.val)
        
        elif root.left is not None and root.right is not None :
            path_sum = max(r_pathsum, l_pathsum, root.val, root.val + r_sum, root.val + l_sum, r_sum + root.val + l_sum)
            return path_sum, max(root.val, root.val + r_sum, root.val + l_sum)
        
        
        
        
        
        
        
        
        
        
        