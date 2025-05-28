class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        mx, my = (p1[0]+p2[0]+p3[0]+p4[0])/4, (p1[1]+p2[1]+p3[1]+p4[1])/4

        dx, dy = p1[0]-mx, p1[1]-my
        targets = [[mx-dy, my+dx], [mx-dx, my-dy], [mx+dy, my-dx]]
        
        if dx == 0 and dy == 0:
            return False

        cnt = 0
        for target in targets:
            for p in [p2,p3,p4]:
                if target[0] == p[0] and target[1] == p[1]:
                    cnt += 1
                
        return cnt == 3

        


