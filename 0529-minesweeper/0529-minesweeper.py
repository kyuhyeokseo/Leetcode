class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        M, N = len(board), len(board[0])
        X, Y = click[0], click[1]

        if board[X][Y] == 'M':
            board[X][Y] = 'X'
            return board
        
        currs = [[X,Y]]
        while currs:
            t = currs.pop(0)
            x, y = t[0], t[1]

            if board[x][y] == 'E':
                
                cnt = 0
                for _, d in enumerate([[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]):
                    dx, dy = d[0], d[1]
                    nX, nY = x+dx, y+dy
                    if 0 <= nX and nX < M and 0 <= nY and nY < N:
                        if board[nX][nY] == 'M':
                            cnt += 1
                if cnt > 0:
                    board[x][y] = str(cnt)
                else:
                    board[x][y] = 'B'
                    for _, d in enumerate([[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]):
                        dx, dy = d[0], d[1]
                        nX, nY = x+dx, y+dy
                        if 0 <= nX and nX < M and 0 <= nY and nY < N:
                            if board[nX][nY] == 'E':
                                currs.append([nX, nY])
        
        return board



