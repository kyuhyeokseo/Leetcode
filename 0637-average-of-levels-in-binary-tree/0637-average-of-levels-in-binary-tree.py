# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if root is None :
            return []
        
        ans = []
        
        tmp = [root]
        while (True) :
            tmp2 = []
            mean = []
            for node in tmp :
                if node.left is not None :
                    tmp2.append(node.left)
                if node.right is not None :
                    tmp2.append(node.right)
                mean.append(node.val)
            ans.append(sum(mean)/len(mean))
            
            tmp = tmp2
            if len(tmp) == 0 :
                break
        
        return ans
        
        
        
        
        