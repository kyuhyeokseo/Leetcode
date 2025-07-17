# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        vals = []

        def findValue(root):

            if root is None:
                return True
            
            findValue(root.left)
            vals.append(root.val)
            findValue(root.right)

            return True
        
        findValue(root)

        vals = list(set(vals))
        vals.sort()

        if len(vals) < 2:
            return -1
        else:
            return vals[1]
        