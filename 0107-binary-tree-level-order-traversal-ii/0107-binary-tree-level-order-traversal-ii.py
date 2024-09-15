# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None :
            return None
        
        elif root.left is None and root.right is None :
            return [[root.val]]
        
        elif root.left is None and root.right is not None :
            
            R = self.levelOrderBottom(root.right)
            R.append([root.val])
            return R
        
        elif root.left is not None and root.right is None :
            
            L = self.levelOrderBottom(root.left)
            L.append([root.val])
            return L
        
        elif root.left is not None and root.right is not None :
            
            L = self.levelOrderBottom(root.left)
            R = self.levelOrderBottom(root.right)
            
            tmp = [[] for _ in range(max(len(L), len(R)))]
            
            if len(L) >= len(R) :
                
                for i in range(len(L)):
                    
                    if i < len(R) :
                        tmp[len(L)-1-i] += (L[-1-i] + R[-1-i])
                    
                    else :
                        tmp[len(L)-1-i] += (L[-1-i])
            
            else :
                
                for i in range(len(R)):
                    
                    if i < len(L) :
                        tmp[len(R)-1-i] += (L[-1-i] + R[-1-i])
                    
                    else :
                        tmp[len(R)-1-i] += (R[-1-i])
            
            tmp.append([root.val])
            
            return tmp
        
        return False
            
            
            
            
            
        
        
        
        