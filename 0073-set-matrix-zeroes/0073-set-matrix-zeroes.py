class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c = set(), set()
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
        
        for rr in r:
            for j in range(N):
                matrix[rr][j] = 0
        
        for cc in c:
            for i in range(M):
                matrix[i][cc] = 0
                