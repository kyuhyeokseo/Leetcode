class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        if n == 1 :
            return 1
        
        cnt = 1
        ans = 1
        L2 = [1]
        L3 = [1]
        L5 = [1]
        
        while True :
            
            n2, n3, n5 = L2[0], L3[0], L5[0]
            
            if 2 * n2 == min(2*n2, 3*n3, 5*n5):
                L2.append(2*n2)
                L3.append(2*n2)
                L5.append(2*n2)
                L2 = L2[1:]
                cnt += 1
                ans = 2 * n2
                
            elif 3 * n3 == min(2*n2, 3*n3, 5*n5):
                #L2.append(3*n3)
                L3.append(3*n3)
                L5.append(3*n3)
                L3 = L3[1:]
                cnt += 1
                ans = 3 * n3
            
            elif 5 * n5 == min(2*n2, 3*n3, 5*n5):
                #L2.append(2*n2)
                #L3.append(2*n2)
                L5.append(5*n5)
                L5 = L5[1:]
                cnt += 1
                ans = 5 * n5
            
            if cnt == n :
                return ans
        
    
            
        
        
        
        
        
        
        