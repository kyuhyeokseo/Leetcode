# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        ret = []

        if root is None:
            return ret
        
        currs = [root]

        while currs:
            nexts = []
            MAX = currs[0].val
            for curr in currs:
                MAX = max(MAX, curr.val)
                if curr.left:
                    nexts.append(curr.left)
                if curr.right:
                    nexts.append(curr.right)
            currs = nexts[:]
            ret.append(MAX)
        
        return ret