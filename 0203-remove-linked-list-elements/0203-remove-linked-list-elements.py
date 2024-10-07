# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if head is None :
            return head
        
        fake = ListNode()
        fake.next = head
        
        curr = fake
        curr_next = curr.next
        
        while curr and curr_next :
            #print('------')
            #print(curr.val, curr_next.val)
            while curr_next and curr_next.val == val :
                curr_next = curr_next.next
            curr.next = curr_next
            if curr_next is not None :
                curr_next = curr_next.next
            curr = curr.next

        return fake.next
        
        
        
        
        
        