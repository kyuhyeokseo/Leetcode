# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None :
            return head
        if head.next is None :
            return head
        
        p = None
        c = head
        n = c.next
        
        while c :
            n = c.next
            c.next = p
            
            p = c
            c = n
        
        return p