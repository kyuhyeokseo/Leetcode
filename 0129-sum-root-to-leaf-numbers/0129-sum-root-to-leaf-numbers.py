# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if root is None :
            return None
        
        ret = 0
        tmp = [root]
        
        while(True) :
            tmp2 = []
            for v in tmp :
                if v.left is None and v.right is None :
                    ret += v.val
                elif v.left is None and v.right is not None :
                    v.right.val += v.val * 10
                    tmp2.append(v.right)
                elif v.left is not None and v.right is None :
                    v.left.val += v.val * 10
                    tmp2.append(v.left)
                else :
                    v.left.val += v.val * 10
                    v.right.val += v.val * 10
                    tmp2.append(v.left)
                    tmp2.append(v.right)
            tmp = tmp2
            if len(tmp) == 0 :
                return ret
        
        
        
        
        
        
        
        
        
        