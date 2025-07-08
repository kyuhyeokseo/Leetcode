class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        M, N = len(img), len(img[0])
        ret = [[0 for _ in range(N)] for _ in range(M)]

        for m in range(M):
            for n in range(N):

                val = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        x, y = m+dx, n+dy
                        if x>=0 and x<M and y>=0 and y<N:
                            ret[m][n] += img[x][y]
                            val += 1
                ret[m][n] //= val
        
        return ret