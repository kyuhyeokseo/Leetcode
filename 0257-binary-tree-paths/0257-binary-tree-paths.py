# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        if root is None :
            return []
        
        
        leftL = self.binaryTreePaths(root.left)
        rightL = self.binaryTreePaths(root.right)
        
        ret = []
        
        if len(leftL) == 0 and len(rightL) == 0 :
            ret.append(f'{root.val}')
        else :
            if len(rightL) != 0 :
                for x in rightL :
                    ret.append(f'{root.val}->' + x)
            if len(leftL) != 0 :
                for x in leftL :
                    ret.append(f'{root.val}->' + x)
        
        return ret
        