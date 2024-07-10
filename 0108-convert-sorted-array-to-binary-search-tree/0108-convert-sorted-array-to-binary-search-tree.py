# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        #print(nums)
        
        if len(nums) == 1 :
            currNode = TreeNode(nums[0], None, None)
            return currNode
        elif len(nums) == 2 :
            currNode = TreeNode(nums[1], self.sortedArrayToBST([nums[0]]), None)
            return currNode
        
        idx_center = len(nums)//2
        center = TreeNode(nums[idx_center], self.sortedArrayToBST(nums[:idx_center]), self.sortedArrayToBST(nums[idx_center+1:]))     
        return center
        
        