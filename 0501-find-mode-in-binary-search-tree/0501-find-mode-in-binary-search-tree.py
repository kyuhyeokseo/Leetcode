# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []
        
        self.L_to_R = []

        lefts = self.l2r(root.left)
        rights = self.l2r(root.right)
        self.L_to_R = lefts[:] + [root] + rights[:]

        curr_val, cnt = None, 0
        max_vals, max_cnt = [10000000], -1

        for node in self.L_to_R:
            if curr_val is None:
                curr_val = node.val
                cnt += 1
            else:
                if curr_val != node.val:
                    if cnt == max_cnt:
                        max_vals.append(curr_val)
                    elif cnt > max_cnt:
                        max_vals = [curr_val]
                        max_cnt = cnt

                    curr_val = node.val
                    cnt = 1
                else:
                    cnt += 1
                    
        if cnt == max_cnt:
            max_vals.append(curr_val)
        elif cnt > max_cnt:
            max_vals = [curr_val]
            max_cnt = cnt

        return max_vals

    def l2r(self, root):
        
        if root is None:
            return []
        
        lefts = self.l2r(root.left)
        rights = self.l2r(root.right)
        return lefts[:] + [root] + rights[:]