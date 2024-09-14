# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):

        self.node1 = None
        self.node2 = None
        
        self.node_tmp = TreeNode(-(1<<31)-1)
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        
        tmp = self.node1.val
        self.node1.val = self.node2.val
        self.node2.val = tmp
        
        
    def inorder(self, root):
        
        if root is None :
            return None
        
        self.inorder(root.left)
        
        if self.node1 is None and self.node_tmp.val >= root.val :
            self.node1 = self.node_tmp
        
        if self.node1 is not None and self.node_tmp.val>= root.val :
            self.node2 = root
            
        self.node_tmp = root
        
    
        self.inorder(root.right)