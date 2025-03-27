# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return None
        ret = root.val

        curr_levels = [root]
        
        while curr_levels:
            ret = curr_levels[0].val
            nxt_levels = []
            for curr in curr_levels:
                if curr.left:
                    nxt_levels.append(curr.left)
                if curr.right:
                    nxt_levels.append(curr.right)
            curr_levels = nxt_levels[:]

        return ret