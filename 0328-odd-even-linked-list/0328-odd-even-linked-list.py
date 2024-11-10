# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        odd_temp = ListNode()
        even_temp = ListNode()
        
        if head is None :
            return None
        elif head.next is None :
            return head
        
        odd_temp.next = head
        even_temp.next = head.next
        
        odd_curr = head
        even_curr = head.next
        
        curr = head.next.next
        
        idx = 1
        
        while curr is not None :
            
            if idx == 1 :
                odd_curr.next = curr
                odd_curr = odd_curr.next
            elif idx == 0 :
                even_curr.next = curr
                even_curr = even_curr.next
            
            curr = curr.next
            idx = idx ^ 1
        
        even_curr.next = None
        odd_curr.next = even_temp.next
        return odd_temp.next
        
        