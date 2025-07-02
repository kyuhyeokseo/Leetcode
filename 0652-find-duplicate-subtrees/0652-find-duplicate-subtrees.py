# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.seen = collections.defaultdict(int)
        self.ret = []

        self.dfs(root)
        return self.ret
        
    def dfs(self, root):
        ret = []
        if root is None:
            return ''
        else:
            ret = str(root.val) + '//' + self.dfs(root.left) + '//' + self.dfs(root.right)
            if ret in self.seen and self.seen[ret] == 1:
                self.ret.append(root)
            self.seen[ret] += 1
            return ret
        
        