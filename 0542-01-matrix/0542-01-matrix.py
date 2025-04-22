class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        borders = []

        M, N = len(mat), len(mat[0])

        def neighZero(x, y):
            if x > 0:
                if mat[x-1][y] == 0:
                    return True
            if x < M-1:
                if mat[x+1][y] == 0:
                    return True
            if y > 0:
                if mat[x][y-1] == 0:
                    return True
            if y < N-1:
                if mat[x][y+1] == 0:
                    return True
            return False

        ret = [[0 for _ in range(N)] for _ in range(M)]

        for i in range(M):
            for j in range(N):
                if mat[i][j] == 1 and neighZero(i,j):
                    ret[i][j] = 1
                    borders.append(str(i) + '_' + str(j))
        
        while borders:
            #print(borders)
            s = set()
            for b in borders:
                tmp = b.split('_')
                x, y = int(tmp[0]), int(tmp[1])

                for diff in [[0,1], [0,-1], [1,0], [-1,0]]:
                    dx, dy = diff[0], diff[1]
                    if x+dx >= 0 and x+dx < M and y+dy >= 0 and y+dy < N:
                        if mat[x+dx][y+dy] == 1 and ret[x+dx][y+dy] == 0:
                            ret[x+dx][y+dy] = ret[x][y] + 1
                            s.add(str(x+dx) + '_' + str(y+dy))
            
            borders = list(s)

        return ret


