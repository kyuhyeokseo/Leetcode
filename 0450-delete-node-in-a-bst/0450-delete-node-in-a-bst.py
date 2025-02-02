# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root is None :
            return None
        
        parent = None
        curr = root

        while curr and curr.val != key :
            if curr.val < key :
                parent = curr
                curr = curr.right
            elif curr.val > key :
                parent = curr
                curr = curr.left
            else :
                break
        
        if curr is None :
            return root
        
        target = curr
        # Case 1 : No Child
        if target.left is None and target.right is None :
            if parent is None :
                return None
            else :
                if parent.left == target :
                    parent.left = None
                else :
                    parent.right = None
                return root
        # Case 2 : One Child
        elif target.left and target.right is None :
            l_child = target.left
            target.val = l_child.val
            target.right = l_child.right
            target.left = l_child.left
            return root
        elif target.left is None and target.right :
            r_child = target.right
            target.val = r_child.val
            target.right = r_child.right
            target.left = r_child.left
            return root
        # Case 3 : Two Children
        elif target.left and target.right :
            parent = target
            curr = target.left
            while curr.right :
                parent = curr
                curr = curr.right
            
            target.val = curr.val

            if curr.left is None and curr.right is None :
                if parent.left == curr :
                    parent.left = None
                else :
                    parent.right = None
            elif curr.left and curr.right is None :
                l_child = curr.left
                curr.val = l_child.val
                curr.right = l_child.right
                curr.left = l_child.left
            elif curr.left is None and curr.right :
                r_child = curr.right
                curr.val = l_child.val
                curr.right = l_child.right
                curr.left = l_child.left
            
            return root
