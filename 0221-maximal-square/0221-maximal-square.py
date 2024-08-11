class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        flag = True
        out = 0
        
        P = []
        for x in matrix:
            P.append(x.copy())
        
        
        while flag :
            
            flag = False
            M,N = len(P), len(P[0])
            
            for m in range(M):
                for n in range(N):
                    
                    if P[m][n] == '1' :
                        flag = True
            
            if flag :
                out += 1
            else :
                return out * out
            
            if M == 1 or N == 1 :
                return out * out
            
            Q = []
            for x in P:
                Q.append(x.copy())

            P = []
            for m in range(M-1) :
                tmp = []
                for n in range(N-1) :
                    if Q[m][n] == '1' and Q[m][n+1] == '1' and Q[m+1][n] == '1' and Q[m+1][n+1] == '1':
                        tmp.append('1')
                    else :
                        tmp.append('0')
                P.append(tmp)
        
        
            
            
            
        
        
        
        
        
        