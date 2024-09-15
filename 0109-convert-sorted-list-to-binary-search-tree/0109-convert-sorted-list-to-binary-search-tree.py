# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def middle(curr = None):
            if curr:
                prev, slow, fast = curr, curr, curr
                
                while fast and fast.next :
                    prev = slow
                    slow = slow.next
                    fast = fast.next.next
                
                return prev, slow
        
        def helper(curr = None):
            
            if curr is None :
                return None
            
            if curr.next is None :
                return TreeNode(curr.val)
            
            pre, mid = middle(curr)
            pre.next = None
            
            out = TreeNode(mid.val)
            
            rootL = helper(curr)
            rootR = helper(mid.next)
            
            #print('----------------')
            #print(mid)
            #print(rootL, rootR)
            
            out.left = rootL
            out.right = rootR
            return out
            
        return helper(head)
        
        
        