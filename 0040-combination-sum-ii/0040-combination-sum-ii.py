class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        D = {}
        for N in candidates :
            if N in D :
                D[N] += 1
            else :
                D[N] = 1
            
        candidates = list(set(candidates))
        candidates.sort(reverse=True)
        
        out = []
        
        X = [[0]]
        
        for i in range(len(candidates)) :
            N = candidates[i]
            
            X_tmp = []
            for n_list in X :
                
                S = n_list[0]
                n_list_cpy = n_list[:]
                
                X_tmp.append(n_list_cpy[:])
                
                for k in range(1, D[N]+1):
                
                    if k*N + S < target :
                    
                        n_list_cpy[0] += N
                        n_list_cpy.append(N)
                        X_tmp.append(n_list_cpy[:])
                    
                    elif k*N + S == target :
                        n_list_cpy.append(N)
                        out.append(n_list_cpy[1:])
                        
            X = X_tmp[:]
        
        print(out)
        return out                
                        
                        
                        
            