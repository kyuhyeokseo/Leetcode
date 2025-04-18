# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return root
        
        self.MakeGreaterTree(root, 0)
        return root

    def MakeGreaterTree(self, node, s):

        #print(f'MakeGraterTree ({node.val if node else 999999}, {s})')

        if node is None:
            return s
        
        afterRight = self.MakeGreaterTree(node.right, s)
        tmp = node.val
        node.val += afterRight
        s = node.val
        afterLeft = self.MakeGreaterTree(node.left, s)

        #print(f'CURR NODE : {tmp} -> {node.val}')
        #print(f'RETURN : {afterLeft}')

        return afterLeft
        


        