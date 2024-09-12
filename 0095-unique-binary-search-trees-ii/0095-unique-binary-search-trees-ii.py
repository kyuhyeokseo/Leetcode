# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        return self.subTree(1, n)
        
        
            
            
    
    def subTree(self, srt, n) :
        
        if n == 0 :
            return None
        
        elif n == 1 :
            return [TreeNode(srt, None, None)]
        
        else :
            tmp = []
            for i in range(0, n):
                if i == 0 :
                    L = None
                    R = self.subTree(srt+i+1, n-i-1)
                elif i == n-1 :
                    L = self.subTree(srt, i)
                    R = None
                else :
                    L = self.subTree(srt, i)
                    R = self.subTree(srt+i+1, n-i-1)
                
                if L is not None and R is not None :
                    for X in L :
                        for Y in R :
                            new = TreeNode(srt+i, X, Y)
                            tmp.append(new)
                
                elif L is None and R is not None :
                    for Y in R :
                        new = TreeNode(srt+i, None, Y)
                        tmp.append(new)
                            
                elif L is not None and R is None :
                    for X in L :
                        new = TreeNode(srt+i, X, None)
                        tmp.append(new)
            return tmp[:]
            
            
        
        
        
        