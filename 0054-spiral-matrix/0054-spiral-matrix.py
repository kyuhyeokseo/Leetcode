import copy

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        CHK = 101
        ans = []
        direction = 0

        matrix_cpy = copy.deepcopy(matrix)
        
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, 0
        
        for _ in range(m*n):
            ans.append(copy.deepcopy(matrix_cpy[i][j]))
            matrix[i][j] = CHK
            print(i,j)
            if (j==n-1 and direction == 0) :
                i += 1
                direction = 1

            elif j<n-1 and direction == 0:
                if (matrix[i][j+1] == CHK) :
                    i += 1
                    direction = 1
                else :
                    j += 1

            elif i==m-1 and direction == 1:
                j -= 1
                direction = 2
            
            elif i<m-1 and direction == 1:
                if matrix[i+1][j] == CHK:
                    j -= 1
                    direction = 2    
                else :
                    i += 1

            elif (j==0 and direction == 2) :
                i -= 1
                direction = 3

            elif j>0 and direction == 2:
                if (matrix[i][j-1] == CHK) :
                    i -= 1
                    direction = 3
                else :
                    j -= 1
                
            elif i >0 and direction == 3:
                if matrix[i-1][j] == CHK:
                    j += 1
                    direction = 0
                else :
                    i -= 1
                
                
        return ans