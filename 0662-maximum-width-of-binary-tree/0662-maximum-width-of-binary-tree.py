# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0

        ret = 1
        currs = [(root, 0)]

        while currs:
            currs_cpy = []
            L, R = -1, -1
            for i, curr in enumerate(currs):
                node, num = curr[0], curr[1]
                if i == 0:
                    L = num
                elif i == len(currs) - 1:
                    R = num
                    ret = max(ret, R-L+1)
                
                if node.left:
                    currs_cpy.append((node.left, 2*num))
                if node.right:
                    currs_cpy.append((node.right, 2*num+1))
                
            currs = currs_cpy[:]
        
        return ret