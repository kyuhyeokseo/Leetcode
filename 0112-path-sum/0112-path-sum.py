# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None :
            return None
        
        tmp = [root]
        self.same = 0
        self.check_sum(tmp, targetSum)
        if self.same == 1 :
            return True
        else :
            return False
    
    
    def check_sum(self, node_list, targetSum) :
        L = len(node_list)
        if L == 0 :
            return True
        
        tmp = []
        for i in range(L):
            root = node_list[i]
            #print('-------------')
            #print(root.val)
            if root.left is not None :
                root.left.val += root.val
                tmp.append(root.left)
                
            if root.right is not None :
                root.right.val += root.val
                tmp.append(root.right)
                
            if root.left is None and root.right is None :
                if root.val == targetSum :
                    self.same = 1
                    
        self.check_sum(tmp, targetSum)
        