class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dd = {}
        for s in strs :
            d = {}
            for i in range(len(s)):
                if s[i] in d :
                    d[s[i]] += 1
                else :
                    d[s[i]] = 1
            dd[s] = d

        ans = []
        for s in strs :
            if len(ans) == 0:
                ans.append([s])
            else :
                find = 0
                for each_list in ans :
                    sample = each_list[0]
                    if dd[sample] == dd[s] :
                        each_list.append(s)
                        find = 1
                        break
                if find == 0 :
                    ans.append([s])
                
        return ans      
        
        
        
        
        
        
        
        
        