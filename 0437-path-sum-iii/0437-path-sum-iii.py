# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        cnt = 0
        if root is None :
            return cnt
        
        self.targetSum = targetSum

        S = targetSum - root.val

        leftcnt = self.pathSum_custom(root.left, [self.targetSum, S])
        rightcnt = self.pathSum_custom(root.right, [self.targetSum, S])
        ret = leftcnt + rightcnt
        if S == 0 :
            return ret + 1
        else :
            return ret


    def pathSum_custom(self, root, sumList):

        if root is None :
            return 0

        cnt = 0
        newSumList = [self.targetSum]
        for s in sumList :
            newSumList.append(s - root.val)
            if s - root.val == 0 :
                cnt += 1
        
        cnt += self.pathSum_custom(root.left, newSumList[:])
        cnt += self.pathSum_custom(root.right, newSumList[:])
        
        return cnt

        

        