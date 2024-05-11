# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if root is None :
            return 0
        
        count = 0
        current = root
 
        while current:
            if current.left is None:
                count += 1
                current = current.right
            else:
                prev = current.left
                while prev.right and prev.right != current:
                    prev = prev.right

                if prev.right is None:
                    prev.right = current
                    current = current.left
                else:
                    prev.right = None
                    count += 1
                    current = current.right

        return count
        
        