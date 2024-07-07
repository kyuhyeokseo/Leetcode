class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.M = len(board)
        self.N = len(board[0])
        self.word = word
        self.flag = False
        self.board = []
        
        self.direction = [[1,0], [-1,0], [0,1], [0,-1]]
        
        for i in range(len(board)) :
            self.board.append(board[i][:])
        
        start = []
        
        for m in range(self.M) :
            for n in range(self.N) :
                if self.board[m][n] == word[0] :
                    start.append([m,n])
        
        if len(start) == 0 :
            return False
        
        
        for tmp in start:
            srtM, srtN = tmp[0], tmp[1]
            #print(f'------ start!! {srtM}, {srtN} ------')
            
            if len(self.word) == 1 :
                self.flag = True
            
            self.board[srtM][srtN] = False
            self.nextStep(1, srtM, srtN)
                
            
            self.board = []
            for i in range(len(board)) :
                self.board.append(board[i][:])
            
        return self.flag
    
        
        
    def nextStep(self, idx, x, y) :
        
        if idx == len(self.word) :
            self.flag = True
            
        if idx >= len(self.word) :
            return True
            
        target = self.word[idx]
        
        for item in self.direction :
            
            newX, newY = x + item[0], y + item[1]
            if 0 <= newX and 0<= newY and newX < self.M and newY < self.N :
                if self.board[newX][newY] == target :
                    self.board[newX][newY] = False
                    self.nextStep(idx+1, newX, newY)
                    self.board[newX][newY] = target
            
        
        
        
        
        
        
        
        
        