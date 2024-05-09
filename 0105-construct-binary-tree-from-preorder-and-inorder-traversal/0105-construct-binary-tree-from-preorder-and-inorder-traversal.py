# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        L = len(preorder)
        
        if L == 0 :
            return None
        
        root_num = preorder[0]
        
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
                ans.right = self.buildTree(preorder[1:], inorder[1:])
                return ans
                
            elif idx == L-1 :
                ans.left = self.buildTree(preorder[1:], inorder[:-1])
                return ans
                
            else :
                pre_left_idx = 1
                pre_right_idx = idx+1
                in_left_idx = idx-1
                in_right_idx = idx+1
                ans.left = self.buildTree(preorder[1:pre_right_idx], inorder[:idx])
                ans.right = self.buildTree(preorder[pre_right_idx:], inorder[in_right_idx:])
                return ans
        
        
        