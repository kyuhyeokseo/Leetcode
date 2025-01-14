"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if root is None :
            return []

        ret = []
        lv_list = [root]

        while lv_list :

            lv_list_cpy = []
            tmp = []
            for curr in lv_list:
                tmp.append(curr.val)
                if curr.children :
                    for chl in curr.children:
                        lv_list_cpy.append(chl)
            
            ret.append(tmp[:])
            lv_list = lv_list_cpy[:]
        
        return ret