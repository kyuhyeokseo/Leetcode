class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        ret = 0
        L = len(points)
        if L < 3 :
            return ret
        
        D = {}
        for i in range(0, L):
            for j in range(0, L):
                if i == j :
                    continue
                
                x1, y1, x2, y2 = points[i][0], points[i][1], points[j][0], points[j][1]
                d_square = (x1-x2) ** 2 + (y1-y2) ** 2

                if i in D :
                    if d_square in D[i] :
                        ret += D[i][d_square]
                        D[i][d_square] += 1
                    else :
                        D[i][d_square] = 1
                else :
                    D[i] = {}
                    D[i][d_square] = 1
                
        return ret * 2




