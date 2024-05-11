# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
          
        self.inorder = self.make_inorder(root)
        self.L = len(self.inorder)
        self.idx = -1
        #print(self.inorder)
        #print(self.L)
        #print('------------')
        
    def next(self) -> int:
        
        self.idx += 1
        ret = self.inorder[self.idx].val
        return ret

    def hasNext(self) -> bool:
        #print(self.idx)
        if self.idx < self.L-1 :
            return True
        else :
            return False
        
        
    def make_inorder(self, root) :
        
        if root.left is None and root.right is None :
            return [root]
        
        elif root.left is None and root.right is not None :
            r = self.make_inorder(root.right)
            return ([root] + r)
        
        elif root.left is not None and root.right is None :
            l = self.make_inorder(root.left)
            return (l + [root])
        
        elif root.left is not None and root.right is not None :
            l = self.make_inorder(root.left)
            r = self.make_inorder(root.right)
            return (l + [root] + r)
        
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()