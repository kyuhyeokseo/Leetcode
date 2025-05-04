"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root is None:
            return 0
        
        ret = 0

        currs = [root]

        while currs:
            ret += 1
            tmps = []
            for curr in currs:
                if curr.children:
                    for child in curr.children:
                        tmps.append(child)
            
            currs = tmps[:]
        
        return ret