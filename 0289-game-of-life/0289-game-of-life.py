class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        tmp_save = []
        for i in range(M):
            tmp = []
            for j in range(N):
                me = board[i][j]
                nei = self.get_neighbor(board, i, j, M, N)
                if me == 1:
                    if nei < 2 :
                        tmp.append(0)
                    elif nei <= 3 :
                        tmp.append(1)
                    else :
                        tmp.append(0)
                elif me == 0:
                    if nei == 3:
                        tmp.append(1)
                    else :
                        tmp.append(0)
            tmp_save.append(tmp)
        
        for i in range(M):
            for j in range(N):
                board[i][j] = tmp_save[i][j]
        
        
        
        
    def get_neighbor(self, board, i, j, M, N):
        ans = 0
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if (i+x) >= 0 and (i+x)<M and (j+y)>=0 and (j+y)<N:
                    if x!= 0 or y!= 0:
                        if board[i+x][j+y] == 1:
                            ans += 1
        return ans