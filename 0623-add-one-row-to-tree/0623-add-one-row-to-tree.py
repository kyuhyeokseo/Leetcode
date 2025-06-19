# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if root is None:
            return TreeNode(val)

        if depth == 1:
            T = TreeNode(val, root, None)
            return T

        curs = [root]
        for _ in range(depth-2):
            curs_cpy = []
            for cur in curs:
                if cur.left:
                    curs_cpy.append(cur.left)
                if cur.right:
                    curs_cpy.append(cur.right)
            curs = curs_cpy[:]
        
        for cur in curs:
            L, R = cur.left, cur.right
            cur.left = TreeNode(val, L, None)
            cur.right = TreeNode(val, None, R)
        
        return root