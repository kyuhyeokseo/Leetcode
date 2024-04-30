class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # H:0, V:1, S:2
        check = [[[0 for _ in range(9)] for _ in range(9)]  for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item.isnumeric() :
                    item = int(item) - 1
                    if check[0][i][item] != 0:
                        return False
                    elif check[0][i][item] == 0:
                        check[0][i][item] += 1
                    
                    if check[1][j][item] != 0:
                        return False
                    else :
                        check[1][j][item] += 1
                    
                    temp = (j//3) + 3 * (i//3)
                    if check[2][temp][item] != 0:
                        return False
                    else :
                        check[2][temp][item] += 1
        
        return True