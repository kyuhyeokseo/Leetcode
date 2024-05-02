class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        x = 'a'
        d = {}
        s_list = []
        for i in range(len(s)):
            if s[i] in d :
                s_list.append(d[s[i]])
            else :
                s_list.append(x)
                d[s[i]] = x
                x = chr(ord(x) + 1)

        x = 'a'
        d = {}
        t_list = []
        for i in range(len(t)):
            if t[i] in d :
                t_list.append(d[t[i]])
            else :
                t_list.append(x)
                d[t[i]] = x
                x = chr(ord(x) + 1)
        
        #print(s_list, t_list)

        if len(s_list) != len(t_list) :
            return False
        
        for idx in range(len(s_list)):
            if s_list[idx] != t_list[idx]:
                return False
        
        return True
