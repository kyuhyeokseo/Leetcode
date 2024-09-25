class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        D = {}
        L = len(s)
        
        for word in wordDict:
            D[word] = 0
        
        path_list = [[] for _ in range(L+1)]
        
        for i in range(L) :
            #print(f'--------- {i} ---------')
            for j in range(i, L):
            
                target = s[i:j+1]
                
                if i == 0 :
                    if target in D:
                        path_list[j+1].append([target[:]])
                        #print(j+1, path_list[j+1])
                else :
                    if len(path_list[i]) != 0 :
                        if target in D:
                            #print('path', path_list[i])
                            for path in path_list[i]:
                                path_copy = path[:]
                                path_copy.append(target[:])
                                path_list[j+1].append(path_copy[:])
                                #print(j+1, path_list[j+1])
        
        #print('-' * 10)
        #for i in path_list :
            #print(i)
        
        if len(path_list[-1]) == 0 :
            return []
        else :
            out = []
            for ans in path_list[-1]:
                out.append(' '.join(ans))
        
            return out
        
        
        