# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        if root is None:
            return [[""]]

        H = 0

        currs = [root]
        while currs:
            H += 1
            currs_cpy = []
            for curr in currs:
                if curr.left:
                    currs_cpy.append(curr.left)
                if curr.right:
                    currs_cpy.append(curr.right)
            currs = currs_cpy
        
        N = (1<<(H))-1
        ret = [["" for _ in range(N)] for _ in range(H)]
        
        B = 1 << (H-1)
        currs = [(root, int(N//2))]
        for h in range(H):
            currs_cpy = []
            for curr in currs:
                node, index = curr[0], curr[1]
                ret[h][index] = str(node.val)
                if node.left:
                    currs_cpy.append((node.left, index-B//2))
                if node.right:
                    currs_cpy.append((node.right, index+B//2))
            B //= 2
            currs = currs_cpy
        
        return ret



