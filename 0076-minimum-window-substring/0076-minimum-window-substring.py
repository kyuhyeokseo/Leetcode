class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        L = len(s)
        for tmp in t:
            if tmp in d:
                d[tmp] += 1
            else :
                d[tmp] = 1
        
        i, j = 0, 0

        for i in range(L):
            if s[i] in d:
                break

        check = {}
        complete = False
        for j in range(i, L):
            chk = 1
            if s[j] in d:
                if s[j] in check:
                    check[s[j]] += 1
                else :
                    check[s[j]] = 1
                
                
                if (len(check.keys()) == len(d.keys())) :
                    for k in check.keys():
                        if check[k] >= d[k] :
                            chk *= 1
                        else :
                            chk *= 0
                    if chk == 1 :
                        complete = True
                        break

        if complete == False :
            return ""

        #print(check)
        #print(d)

        ans = s[i:j+1]

        target = s[i]

        while (True) :
            #print('target, i, j :', target,i,j)
            if check[target] == d[target] :
                j += 1
                if j>=L :
                    return ans
                while (s[j] != target) :
                    if s[j] in d :
                        check[s[j]] += 1
                    j += 1
                    if j >= L :
                        return ans
                check[s[j]] += 1

            check[target] -= 1
            i += 1
            while (s[i] not in d):
                i += 1
            target = s[i]

            if j-i+1 < len(ans):
                ans = s[i:j+1]


