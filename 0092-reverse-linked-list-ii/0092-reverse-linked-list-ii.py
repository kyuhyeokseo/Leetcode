# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right :
            return head
        
        cur = head
        l = head
        r = head
        tmp = 0
        
        val_list = []
        
        for i in range(right) :
            if i == left-1 :
                l = cur
            elif i == right-1 :
                r = cur
                
            if i >= left - 1 and i <= right -1 :
                val_list.append(cur.val)
            
            cur = cur.next
    
        cur = l
        for i in range(right-left +1):
            cur.val = val_list[len(val_list)-1-i]
            cur = cur.next
        
        return head
        
        
        
        
        
        
        
        
        
        