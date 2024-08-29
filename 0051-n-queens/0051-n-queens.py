class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        ans1 = [["." * i + "Q" + "." * (n-1-i)] for i in range(n)]
        
        for now in range(1,n):
            
            ans2 = []
            
            for item in ans1 :
                
                idx_candidate = [True for _ in range(n)]
                
                for floor in range(len(item)) :
                    each = item[floor]
                    q_already = each.find('Q')
                    
                    idx_candidate[q_already] = False
                    
                    if q_already + (now - floor) < n :
                        idx_candidate[q_already + (now - floor)] = False
                        
                    if q_already - (now - floor) >= 0 :
                        idx_candidate[q_already - (now - floor)] = False
                
                for i in range(n) :
                    if idx_candidate[i] :
                        
                        item_copy = item[:]
                        item_copy.append("." * i + "Q" + "." * (n-1-i))
                    
                        ans2.append(item_copy[:])
                
            ans1 = ans2[:]
    
        return ans1
        #for item in ans1 :
        #    for l in item :
        #        print(l)
        #    print()
        
        
        
        
        
        
        