# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None :
            return head
        
        if head.next is None :
            return head
        
        out = ListNode()
        out.val = -9999
        out.next = head
        
        target_next = head.next
        target_prev = out.next
        target = target_next
        
        while target :
            target_next = target_next.next
            
            #print('-' * 20)
            #if target_next is None :
            #    print(target_prev.val, target.val, 'None')
            #else :
            #    print(target_prev.val, target.val, target_next.val)
                
            
            if target.val >= target_prev.val :
                target_prev = target
            else :
                curr = out
                curr_next = out.next
                
                while curr != target_prev :
                    
                    if curr.val <= target.val and target.val <= curr_next.val :
                        curr.next = target
                        target.next = curr_next
                        target_prev.next = target_next
                        
                        break
                    
                    curr = curr.next
                    curr_next = curr_next.next
            
            
            #tmp = out.next
            #print_list = []
            #while tmp :
            #    print_list.append(tmp.val)
            #    tmp = tmp.next
            #print(print_list)
            
            target = target_next
        
        return out.next
                        
                        
                        
                        
                        