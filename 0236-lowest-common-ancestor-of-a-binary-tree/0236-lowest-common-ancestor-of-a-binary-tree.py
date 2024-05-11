# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        find_p = False
        find_q = False
        d = {}
        d[root.val] = []
        
        tmp = [root]
        
        while (len(tmp) != 0) :
            tmp2 = []

            for node in tmp :
                #print(node.val)
                if node.val == p.val :
                    find_p = True
                elif node.val == q.val :
                    find_q = True
                
                if node.left is not None :
                    d[node.left.val] = d[node.val] + [0]
                    tmp2.append(node.left)
                    
                if node.right is not None :
                    d[node.right.val] = d[node.val] + [1]
                    tmp2.append(node.right)
                    
            tmp = tmp2
            if find_p and find_q :
                break
                
        #print('-----------------')
        #print(d)
        
        curr = root
        for i in range(min(len(d[p.val]), len(d[q.val]))) :
    
            if d[p.val][i] == d[q.val][i] :
                if d[p.val][i] == 0 :
                    curr = curr.left
                else :
                    curr = curr.right
            else :
                return curr
            
        return curr 
            
            
            
            
            