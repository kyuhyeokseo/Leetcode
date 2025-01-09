class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        M, N = len(board), len(board[0])
        cnt = 0

        for i in range(M):
            for j in range(N):

                if board[i][j] == 'X' and (i==0 or board[i-1][j]=='.') and (j==0 or board[i][j-1]=='.'):
                    cnt += 1


        return cnt
