# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1 = list1
        cur2 = list2
        ans = ListNode()
        cur = ans
        
        if cur1 is None and cur2 is None :
            return None
        
        while (True) :
        
            if cur1 is None and cur2 is None :
                return ans
            
            elif cur1 is None :
                num2 = cur2.val
                cur.val = num2
                cur2 = cur2.next
                if cur2 is None :
                    return ans
                cur.next = ListNode()
                cur = cur.next
        
            elif cur2 is None :
                num1 = cur1.val
                cur.val = num1
                cur1 = cur1.next
                if cur1 is None :
                    return ans
                cur.next = ListNode()
                cur = cur.next
                
            else :
                num1 = cur1.val
                num2 = cur2.val
                if num1 <= num2 :
                    cur.val = num1
                    cur1 = cur1.next
                else :
                    cur.val = num2
                    cur2 = cur2.next
                cur.next = ListNode()
                cur = cur.next
        
        
        
        
        
        
        
        
        