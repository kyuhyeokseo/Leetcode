# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        
        self.ret = 0
        self.postOrder(root)

        return self.ret

    def postOrder(self, root):
        if root is None:
            return 0
        
        valL = valR = valB = 0
        valL = self.postOrder(root.left)
        valR = self.postOrder(root.right)
    
        if root.left and root.right and root.val == root.left.val == root.right.val:
            self.ret = max(self.ret, valL + valR + 2)
            return max(valL, valR) + 1
        
        elif root.left and root.val == root.left.val:
            valL += 1
            self.ret = max(self.ret, valL)
            return valL
        
        elif root.right and root.val == root.right.val:
            valR += 1
            self.ret = max(self.ret, valR)
            return valR
        
        else:
            return 0


        
        