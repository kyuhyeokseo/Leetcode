# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        c = 0
        cur1 = l1
        cur2 = l2
        ans = ListNode()
        cur = ans
        
        while(True):
            
            if cur1 is None :
                num1 = 0
            else :
                num1 = cur1.val
                
            if cur2 is None :
                num2 = 0
            else :
                num2 = cur2.val
            
            s = (num1 + num2 + c) % 10
            c = (num1 + num2 + c) // 10
            cur.val = s
            
            if cur1 is not None :
                cur1 = cur1.next
            if cur2 is not None :
                cur2 = cur2.next
            
            if cur1 is None and cur2 is None and c == 1 :
                cur.next = ListNode(1)
                return ans
            
            elif cur1 is None and cur2 is None :
                return ans
            
            cur.next = ListNode()
            cur = cur.next

            
            
        
        
        
        
        
        
        
        
        
        
        