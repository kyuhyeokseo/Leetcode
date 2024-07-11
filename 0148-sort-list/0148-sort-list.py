# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None :
            return head
        
        mid = self.divide(head)
        
        left_head = self.sortList(head)
        right_head = self.sortList(mid)
        
        return self.merge(left_head, right_head)
        
        
        
        
    def divide(self, head) :
        
        end = head
        ret = head
        tmp = head
        
        while tmp is not None and tmp.next is not None :
            end = ret
            ret = ret.next
            tmp = tmp.next.next
            
        end.next = None
        return ret
    
    
    def merge(self, left, right) :
        
        fake = ListNode()
        curr = fake
        while (left is not None or right is not None) :
            if (left is not None and ((right is not None and right.val > left.val) or (right is None))):
                curr.next = left
                curr = left
                left = left.next
            else :
                curr.next = right
                curr = right
                right = right.next
        
        return fake.next
        
        
        
        
        