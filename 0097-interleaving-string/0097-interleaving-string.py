class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3) :
            return False
        
        i,j = 0,0
        
        check = [[False for _ in range(len(s2) +1)] for _ in range(len(s1)+1)]
        
        dp = [[0,0]]
        
        while True:
            
            tmp = []
            
            #print(dp)
            if len(dp) == 0 :
                return False
            
            for I, J in dp :
                idx = I+J
                
                if idx < len(s3) :
                    target = s3[idx]
                
                if I == len(s1) and J==len(s2):
                    return True
                
                elif I == len(s1) :
                    if target == s2[J] :
                        
                        if check[I][J+1] == False :
                            tmp.append([I, J+1])
                            check[I][J+1] = True
                
                elif J == len(s2) :
                    if target == s1[I] :
                        
                        if check[I+1][J] == False :
                            tmp.append([I+1, J])
                            check[I+1][J] = True

                else :
                    if target == s1[I] :
                        if check[I+1][J] == False :
                            tmp.append([I+1, J])
                            check[I+1][J] = True
                
                    if target == s2[J] :
                        tmp.append([I, J+1])
                        if check[I][J+1] == False :
                            tmp.append([I, J+1])
                            check[I][J+1] = True
                        
            dp = tmp.copy()
        
        
        