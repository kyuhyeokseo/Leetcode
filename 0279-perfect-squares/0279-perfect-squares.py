class Solution:
    def numSquares(self, n: int) -> int:
        
        V = [False for _ in range(n+1)]
        V[n] = True
        
        num_list = [n]
        
        level = 1
        
        while True :
            
            tmp_list = []
            for num in num_list :
                for i in range(1, int(num ** (1/2))+1):
                    
                    new = num - i*i
                    
                    if new == 0 :
                        return level
                    
                    if V[new] == False :
                        tmp_list.append(num - i*i)
                        V[new] = True
                        
            
            level += 1
            num_list = tmp_list[:]
        
        
        
        
        