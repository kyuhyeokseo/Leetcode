# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is not None:
            if root.val < val:
                if root.right is None:
                    root.right = TreeNode(val, None, None)
                else:
                    root.right = self.insertIntoBST(root.right, val)
            elif root.val > val:
                if root.left is None:
                    root.left = TreeNode(val, None, None)
                else:
                    root.left = self.insertIntoBST(root.left, val)
            
            return root
        
        else:
            return TreeNode(val)