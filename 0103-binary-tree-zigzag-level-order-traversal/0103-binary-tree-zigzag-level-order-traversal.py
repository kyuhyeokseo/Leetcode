# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None :
            return []
        
        ans = []
        zigzag = 1
        
        tmp = [root]
        while (True) :
            tmp2 = []
            t = []
            #print('-------------')
            if zigzag > 0 :
                for node in tmp :
                    #print(node.val)
                    if node.left is not None :
                        tmp2.append(node.left)
                    if node.right is not None :
                        tmp2.append(node.right)

                    t.append(node.val)
            
            else :
                for node in tmp :
                    #print(node.val)
                    if node.right is not None :
                        tmp2.append(node.right)
                    if node.left is not None :
                        tmp2.append(node.left)
                    
                    t.append(node.val)
                
            ans.append(t)
            
            tmp[:] = tmp2[::-1]
            zigzag = - zigzag

            if len(tmp) == 0 :
                break
        
        return ans
        
        
        
        
        
        
        
        
        
        