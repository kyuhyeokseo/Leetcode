class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        Sa = (ax2-ax1) * (ay2-ay1)
        Sb = (bx2-bx1) * (by2-by1)
        
        Ox = min(ax2, bx2) - max(ax1, bx1)
        if Ox < 0 :
            Ox = 0
        Oy = min(ay2, by2) - max(ay1, by1)
        if Oy < 0 :
            Oy = 0
        
        O = Ox * Oy
        
        return Sa + Sb - O
        