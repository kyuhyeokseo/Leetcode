# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        le = ListNode(-101)
        ge = ListNode(-101)
        
        if head is None :
            return None
        
        prev = None
        curr = head
        le_curr = le
        ge_curr = ge
        
        while curr is not None :
            if curr.val < x :
                prev = curr
                curr = curr.next
                le_curr.next = prev
                le_curr = prev
            else :
                prev = curr
                curr = curr.next
                ge_curr.next = prev
                ge_curr = prev
        
        
        le_curr.next = ge.next
        ge_curr.next = None
        
        return le.next
        
        
        
        
        
        