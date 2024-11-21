class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        ans = []
        
        w2i_dic = {}
        for i, w in enumerate(words) :
            w2i_dic[w] = i
        
        for i, w in enumerate(words) :
            for j in range(len(w)+1):
                
                pre, suf = w[:j], w[j:]
                
                if pre[::] == pre[::-1] :
                    if suf[::-1] in w2i_dic :
                        k = w2i_dic[suf[::-1]]
                        if i != k :
                            ans.append([k,i])
                
                if j!= len(w) and suf[::] == suf[::-1] :
                    if pre[::-1] in w2i_dic :
                        k = w2i_dic[pre[::-1]]
                        if i != k :
                            ans.append([i,k])
        
        return ans
            
                
        
        
        
        
        
        