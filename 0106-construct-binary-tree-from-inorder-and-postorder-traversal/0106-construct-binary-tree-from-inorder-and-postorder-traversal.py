# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        L = len(postorder)
        #print('------------')
        #print(inorder)
        #print(postorder)
        
        if L == 0 :
            return None
        
        root_num = postorder[-1]
        #print(root_num)
        
        if L == 1 :
            return TreeNode(root_num)
        
        elif L == 2 :
            ans = TreeNode(root_num)
            if inorder[0] == root_num :
                ans.right = TreeNode(inorder[1])
            else :
                ans.left = TreeNode(inorder[0])
            return ans
        
        else :
            idx = inorder.index(root_num)
            ans = TreeNode(root_num)
            if idx == 0 :
                ans.right = self.buildTree(inorder[1:], postorder[:-1])
                return ans
                
            elif idx == L-1 :
                ans.left = self.buildTree(inorder[:-1], postorder[:-1])
                return ans
                
            else :

                ans.left = self.buildTree(inorder[:idx], postorder[:idx])
                ans.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
                return ans
        
        
        
        
        
        
        
        
        
        