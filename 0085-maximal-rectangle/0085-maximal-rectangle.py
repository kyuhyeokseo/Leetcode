class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        M = len(matrix)
        N = len(matrix[0])
        
        out = 0
        is_zero = 0
        for x in range(M):
            for y in range(N):
                if matrix[x][y] == '1':
                    out = 1
                else :
                    is_zero = 1
        
        
        if out == 0 :
            return 0
        if is_zero == 0 :
            return M*N
        
        P1 = []
        for x in range(M):
            P1.append(matrix[x][:])
        
        w = 1
        for _ in range(M):
            
            print('-'*10)
            P = []
            for x in range(len(P1)):
                P.append(P1[x][:])
                
            ###########################
            
            ############
            #for z in P:
            #    print(z)
            ############
            
            h = 1
            for _ in range(N) :
                flag = False
                X = len(P)
                Y = len(P[0])

                Q = []
                for i in range(X):
                    tmp = []
                    for j in range(Y):
                        if P[i][j] == '1' :
                            flag = True
                        if j < Y-1 :
                            if P[i][j] == '1' and P[i][j+1] == '1' :
                                tmp.append('1')
                            else :
                                tmp.append('0')
                    Q.append(tmp[:])
            
                P = []
                for x in range(len(Q)):
                    P.append(Q[x][:])
                
                if flag == True :
                    out = max(out, w*h)
                else :
                    break
                h += 1
            ##############################
            C = len(P1)
            D = len(P1[0])

            P2 = []
            flag2 = False
            for ii in range(C):
                tmp = []
                for jj in range(D):
                    
                    if P1[ii][jj] == '1' :
                            flag2 = True
                    if ii < C-1 :
                        if P1[ii][jj] == '1' and P1[ii+1][jj] == '1' :
                            tmp.append('1')
                        else :
                            tmp.append('0')
                            
                if ii < C-1 :
                    P2.append(tmp[:])
            
            P1 = []
            for xx in range(len(P2)):
                P1.append(P2[xx][:])
                
            if flag2 == False :
                break
            w += 1
            
        return out
            
            
            
                
            
                