"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':

        ret = Node(False, False, None, None, None, None)

        if quadTree1 is None:
            return quadTree2
        
        if quadTree2 is None:
            return quadTree1

        ret.isLeaf = (quadTree1.isLeaf and quadTree2.isLeaf) or (quadTree1.isLeaf and quadTree1.val) or (quadTree2.isLeaf and quadTree2.val)
        
        ret.val = (quadTree1.val or quadTree2.val) if ret.isLeaf else True

        if not ret.isLeaf:
            ret.topLeft     = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            ret.topRight    = self.intersect(quadTree1.topRight, quadTree2.topRight)
            ret.bottomLeft  = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            ret.bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        
            if ret.topLeft.isLeaf and ret.topRight.isLeaf and ret.bottomLeft.isLeaf and ret.bottomRight.isLeaf:
                if ret.topLeft.val and ret.topRight.val and ret.bottomLeft.val and ret.bottomRight.val:
                    ret.isLeaf = True
                    ret.val = ret.topLeft.val
                    ret.topLeft = ret.topRight = ret.bottomLeft = ret.bottomRight = None
            
                elif not ret.topLeft.val and not ret.topRight.val and not ret.bottomLeft.val and not ret.bottomRight.val:
                    ret.isLeaf = True
                    ret.val = ret.topLeft.val
                    ret.topLeft = ret.topRight = ret.bottomLeft = ret.bottomRight = None
            
        return ret


        
        