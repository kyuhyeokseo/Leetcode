class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        L = len(equations)
        d = {}
        
        for l in range(L) :
            x, y = equations[l][0], equations[l][1]
            if x == y :
                pass
            
            if x in d :
                tmp_d = d[x]
                tmp_d[y] = 1/values[l]
            elif x not in d :
                d[x] = {}
                tmp_d = d[x]
                tmp_d[y] = 1/values[l]
                
            if y in d :
                tmp_d = d[y]
                tmp_d[x] = values[l]
            elif y not in d :
                d[y] = {}
                tmp_d = d[y]
                tmp_d[x] = values[l]
        
        ans = []
        check_d = {}
        for k in d.keys():
            check_d[k] = -1
        
        #print(check_d)
        
        for q in queries :
            #print('-------NEW QUERY ------')
            for k in d.keys():
                check_d[k] = -1
                
            end, srt = q[0], q[1]
            if srt not in d :
                ans.append(-1.00000)
                continue 
                
            elif end not in d :
                ans.append(-1.00000)
                continue
                
            if srt == end :
                ans.append(1.00000)
            else :
                check_d[srt] = 1
                curr_list = [srt]
                find = 0
                
                while (find == 0 and len(curr_list) != 0):
                    #print('--------------')
                    tmp_curr_list = []
                    #print(curr_list)
                    for curr in curr_list :
                        tmp = d[curr]
                        
                        for u in d[curr].keys() :
                            if check_d[u] == -1:
                                tmp_curr_list.append(u)
                                check_d[u] = check_d[curr] * tmp[u]
                            if u == end :
                                find = 1
                                break
                                
                        if find == 1 :
                            break
                    curr_list[:] = tmp_curr_list[:]
                
                ans.append(check_d[end])    
                    
        return ans
        
        