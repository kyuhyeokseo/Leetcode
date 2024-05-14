class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.M = len(board)
        self.N = len(board[0])
        self.ans = []
        self.tmp = []
        
        for i in range(self.M) :
            for j in range(self.N):
                if self.board[i][j] == 'O':
                    surround = self.dfs(i,j)
                    if surround == True :
                        self.tmp = []
                    else :
                        self.ans += self.tmp
        
        for (i,j) in self.ans :
            self.board[i][j] = 'O'
        
        
    def dfs(self, i, j) :
        if i<0 or i>=self.M or j<0 or j>=self.N :
            return False
        
        if self.board[i][j] == 'O':
            self.tmp.append((i,j))
            self.board[i][j] = 'X'
            s1 = self.dfs(i-1, j)
            s2 = self.dfs(i+1, j)
            s3 = self.dfs(i, j-1)
            s4 = self.dfs(i, j+1)
            return s1 and s2 and s3 and s4
            
        return True
        
        