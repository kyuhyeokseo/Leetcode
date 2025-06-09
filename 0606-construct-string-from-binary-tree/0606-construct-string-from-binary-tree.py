# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        ret = ""
        if root is None :
            return ret
        
        ret += str(root.val)
        
        if root.left and root.right:
            ret += "("
            ret += self.tree2str(root.left)
            ret += ")("
            ret += self.tree2str(root.right)
            ret += ")"
            return ret
        elif root.left and not root.right:
            ret += "("
            ret += self.tree2str(root.left)
            ret += ")"
            return ret
        elif not root.left and root.right:
            ret += "()("
            ret += self.tree2str(root.right)
            ret += ")"
            return ret
        else:
            return ret
        
            

