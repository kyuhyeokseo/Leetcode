# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None :
            return []
        
        ans = []
        
        tmp = [root]
        while (True) :
            tmp2 = []
            for node in tmp :
                if node.left is not None :
                    tmp2.append(node.left)
                if node.right is not None :
                    tmp2.append(node.right)
            ans.append(node.val)
            tmp = tmp2
            if len(tmp) == 0 :
                break
        
        return ans
        
        
        
        
        