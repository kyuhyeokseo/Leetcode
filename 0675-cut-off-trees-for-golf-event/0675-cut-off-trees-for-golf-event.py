class Solution:
    def __init__(self):
        self.M, self.N = 0, 0
        self.LIMIT = (1 << 12)
        self.map = None

    def findShortestPath(self, t, srtX, srtY, tarX, tarY):
        
        #print(f'----- find Shortest Path ({srtX}, {srtY}) -> ({tarX}, {tarY})')
        if (srtX, srtY) == (tarX, tarY):
            return 0

        currs = [(srtX, srtY, t * self.LIMIT)]

        while currs:

            X, Y, steps = currs.pop(0)
            self.map[X][Y] = steps

            for dX, dY in [(-1,0), (1,0), (0,1), (0,-1)]:
                x, y = X+dX, Y+dY
                if x >= 0 and x < self.M and y>=0 and y < self.N:
                    if self.map[x][y] != 0 and self.map[x][y] < t * self.LIMIT:
                        if (x,y) == (tarX, tarY):
                            return steps+1 - t*self.LIMIT
                        currs.append((x, y, steps+1))
                        self.map[x][y] = steps+1
        
        return -1
        

    def cutOffTree(self, forest):
        
        self.M, self.N = len(forest), len(forest[0])
        self.LIMIT = 5000
        self.map = [[0 for _ in range(self.N)] for _ in range(self.M)]

        q = []
        for m in range(self.M):
            for n in range(self.N):
                if forest[m][n] >= 1:
                    self.map[m][n] = -1
                if forest[m][n] > 1:
                    q.append([forest[m][n], m, n])
        
        q.sort()
        cnt = 0
        srtX, srtY = 0, 0
        t = 1

        while q:
            tmp = q.pop(0)
            target, tarX, tarY = tmp[0], tmp[1], tmp[2]
            
            s = self.findShortestPath(t, srtX, srtY, tarX, tarY)

            if s == -1:
                return -1
            else:
                cnt += s

            #print(f'START ({srtX}, {srtY}) -> END ({tarX}, {tarY}) : LENGTH {s}\n')
            srtX, srtY = tarX, tarY
            t += 1
        
        return cnt