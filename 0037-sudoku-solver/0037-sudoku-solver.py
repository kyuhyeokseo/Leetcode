class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        flag = True
        for x in range(3) :
            for y in range(3) :
                for i in range(3) :
                    for j in range(3):
                        
                        if board[3*x + i][3*y + j] == '.':
                            flag = False
                            break
                            
                    if flag == False :
                        break
                
                if flag == False :
                    break
                        
            if flag == False :
                break
    
    
        if flag == True :
            return True
        
        else :

            X, Y = x, y
            I, J = 3*x +i, 3*y + j
            
            num_list = [True for i in range(10)]
            
            for k in range(9):
                if board[I][k] != '.':
                    num_list[int(board[I][k])] = False
                if board[k][J] != '.':
                    num_list[int(board[k][J])] = False
            
            for dx in range(3):
                for dy in range(3):
                    if board[3*X + dx][3*Y + dy] != '.':
                        num_list[int(board[3*X + dx][3*Y + dy])] = False
            
            #print(I, J, num_list)
            for new_num in range(1,10,1):
                
                if num_list[new_num]:
                    board[I][J] = str(new_num)
                    out = self.solveSudoku(board)
                    if out :
                        return True
                    else :
                        board[I][J] = '.'
                
            return False
        
        
        