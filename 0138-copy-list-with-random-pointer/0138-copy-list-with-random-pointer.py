"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None :
            return None
        
        o_node_list = []
        node_list = []
        idx_list = []
        cur = head
        ans = Node(0)
        cur_ans = ans
        while (cur is not None):
            o_node_list.append(cur)
            cur_ans.val = cur.val
            if cur.random is None :
                idx_list.append(-1)
            else :
                idx_list.append(cur.random)
                
            cur = cur.next
            if cur is not None :
                cur_ans.next = Node(0)
            node_list.append(cur_ans)
            cur_ans = cur_ans.next
            
        for j in range(len(idx_list)) :
            if idx_list[j] == -1 :
                continue

            idx_list[j] = o_node_list.index(idx_list[j])
        
        
        for i in range(len(node_list)) :
            cur = node_list[i]
            if i < len(node_list)-1 :
                cur.next = node_list[i+1]
                
            if idx_list[i] == -1 :
                cur.random = None
            else :
                cur.random = node_list[idx_list[i]]
        
        return ans
        
        
        
        