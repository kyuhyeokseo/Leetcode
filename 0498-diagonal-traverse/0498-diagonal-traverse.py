class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        ret = []

        s, i = 0, 0

        M, N = len(mat), len(mat[0])

        for _ in range(M*N):

            j = s-i
            ret.append(mat[i][j])
            
            if s%2 == 0:
                if i==0 or j==N-1:
                    s += 1
                    i = max(0, s-N+1)
                else:
                    i -= 1
            else:
                if i==M-1 or j==0:
                    s += 1
                    i = min(M-1, s)
                else:
                    i += 1
        
        return ret







