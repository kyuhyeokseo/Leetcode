class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        M, N = len(matrix), len(matrix[0])
        
        for i in range(M):
            if matrix[i][0] > target :
                break
            
            for j in range(N):
                
                if matrix[i][j] == target :
                    return True
                elif matrix[i][j] > target :
                    break
                
        
        return False
        
        
        
        