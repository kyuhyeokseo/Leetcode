# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        root = None
        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
        elif root1 and not root2:
            root = TreeNode(root1.val)
            root.left = root1.left
            root.right = root1.right
        elif not root1 and root2:
            root = TreeNode(root2.val)
            root.left = root2.left
            root.right = root2.right
        else:
            root = None
        
        return root


