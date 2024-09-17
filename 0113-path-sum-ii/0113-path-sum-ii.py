# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        
        if root is None :
            return []
        
        newTarget = targetSum - root.val
        
        if root.left is None and root.right is None:
            if newTarget == 0:
                return [[root.val]]
            else :
                return None
            
        elif root.left is None and root.right is not None :
            R = self.pathSum(root.right, newTarget)
            
            if R is None :
                return None
            else :
                tmp = []
                for item in R:
                    tmp.append([root.val] + item[:])
                return tmp            
            
        elif root.left is not None and root.right is None :
            L = self.pathSum(root.left, newTarget)
            if L is None :
                return None
            else :
                tmp = []
                for item in L:
                    tmp.append([root.val] + item[:])
                return tmp  
            
        elif root.left is not None and root.right is not None :
            L = self.pathSum(root.left, newTarget)
            R = self.pathSum(root.right, newTarget)
            
            if L is None and R is None :
                return None
            elif L is None and R is not None :
                tmp = []
                for item in R:
                    tmp.append([root.val] + item[:])
                return tmp 
            elif L is not None and R is None :
                tmp = []
                for item in L:
                    tmp.append([root.val] + item[:])
                return tmp 
            else :
                tmp = []
                for item in R:
                    tmp.append([root.val] + item[:])
                for item in L:
                    tmp.append([root.val] + item[:])
                return tmp 
        
            
        
       