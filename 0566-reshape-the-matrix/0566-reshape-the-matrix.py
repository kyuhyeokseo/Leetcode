class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        M, N = len(mat), len(mat[0])

        if r*c != M*N :
            return mat

        ret = [[0 for _ in range(c)] for _ in range(r)]

        for k in range(r*c):
            ret[k//c][k%c] = mat[k//N][k%N]
        
        return ret