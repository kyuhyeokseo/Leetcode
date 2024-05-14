"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node is None :
            return None
        
        self.d = {}
        self.L = 0
        self.get_node_num(node)
        self.node_list = []
        
        M = self.L + 1
        
        for i in range(1, M) :
            self.node_list.append(Node())
            self.node_list[-1].val = i
            
        for i in range(self.L) :
            main_node = self.node_list[i]
            if len(self.d[i+1].neighbors) == 0 :
                pass
            else :
                main_node.neighbors = []
                for j in self.d[i+1].neighbors :
                    
                    main_node.neighbors.append(self.node_list[j.val-1])
        
        return self.node_list[0]
        
        
    def get_node_num(self, node):
        new = 0
        self.d[node.val] = node
        for v in node.neighbors :
            if v.val not in self.d :
                self.get_node_num(v)
                new += 1
        if new == 0 :
            self.L = len(self.d.keys())

            
        
        
        
        
        
        