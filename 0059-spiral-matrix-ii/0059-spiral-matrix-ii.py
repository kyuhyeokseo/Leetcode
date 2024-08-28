class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        N = n * n
        ans = [[0 for _ in range(n)] for _ in range(n)]
        
        ans[0][0] = 1
        
        if n == 1 :
            return ans
        
        x, y = 0, 0
        
        d = [[0,1], [1,0], [0, -1], [-1,0]]
        
        d_idx = 0
        dX, dY = d[d_idx]
        
        for idx in range(N-1) :
            
            num = idx + 2
            
            if x+dX >= 0 and x+dX < n and y+dY >= 0 and y+dY < n :
                
                if ans[x+dX][y+dY] == 0 :
                    x = x+dX
                    y = y+dY
                
                else :
                    d_idx += 1
                    d_idx %= 4
                    dX, dY = d[d_idx]
                    x = x+dX
                    y = y+dY
            else :
                d_idx += 1
                d_idx %= 4
                dX, dY = d[d_idx]
                x = x+dX
                y = y+dY
            #print(x,y,num)
            ans[x][y] = num
        
        #for item in ans :
        #    print(item)
        return ans