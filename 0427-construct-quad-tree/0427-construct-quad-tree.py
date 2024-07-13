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
    def construct(self, grid: List[List[int]]) -> 'Node':
        #print('------------------')
       

        size = len(grid)
        #print(size)
       
        if size == 1 :
            #print(grid[0][0], True)
            return Node(grid[0][0], True, None, None, None, None)
       
        else :
            isleaf = True
            #print(grid)
            tt = grid[0][0]
            for i in range(size):
                for j in range(size):
                    if grid[i][j] == tt :
                        continue
                    else :
                        isleaf = False
           
            if isleaf :
                return Node(tt, isleaf, None, None, None, None)
            else :
                #print(grid)
                tl, tr, bl, br = [], [], [], []
                #print(size)
                for i in range(size) :
                    #print(f'size//2 : {size//2}')
                    #print(f'idx : {i}')
                    if i < size/2 :
                        #print(grid[i])
                        tl.append(grid[i][:int(size/2)])
                        tr.append(grid[i][int(size/2):])
                    else :
                        #print(grid[i])
                        bl.append(grid[i][:int(size/2)])
                        br.append(grid[i][int(size/2):])
                       
                    #print(tl)
                    #print(tr)
                    #print(bl)
                    #print(br)
                top_left_node = self.construct(tl)
                top_right_node = self.construct(tr)
                bottom_left_node = self.construct(bl)
                bottom_right_node = self.construct(br)
               
                return Node(0, False, top_left_node, top_right_node, bottom_left_node, bottom_right_node)

        
        