class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        M, N = len(matrix), len(matrix[0])
        self.acc = [[0 for _ in range(N+1)]]
        
        for m in range(M):
            tmp = [0]
            s = 0
            for n in range(N):
                s += matrix[m][n]

                if m == 0 :
                    tmp.append(s)
                else :
                    tmp.append(s + self.acc[m][n+1])
            self.acc.append(tmp)
        
        #for item in self.acc :
        #    print(item)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        return self.acc[row2+1][col2+1] + self.acc[row1][col1] - self.acc[row1][col2+1] - self.acc[row2+1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)