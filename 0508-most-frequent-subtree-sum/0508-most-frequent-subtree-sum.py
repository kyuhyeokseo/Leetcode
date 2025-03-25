# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        self.D = {}

        S = self.sum_findFrequentTreeSum(root)
        ret = []

        MAX_v = None
        for k, v in self.D.items():
            if MAX_v is None:
                MAX_v = v
            else:
                MAX_v = max(MAX_v, v)
        
        for k in self.D.keys():
            if self.D[k] == MAX_v:
                ret.append(k)
        
        return ret


    def sum_findFrequentTreeSum(self, root):
        
        if root is None:
            return None
        
        Lsum = self.sum_findFrequentTreeSum(root.left)
        Rsum = self.sum_findFrequentTreeSum(root.right)

        key = root.val
        if Lsum:
            key += Lsum
        if Rsum:
            key += Rsum
        
        if key in self.D:
            self.D[key] += 1
        else:
            self.D[key] = 1
        
        return key
            


