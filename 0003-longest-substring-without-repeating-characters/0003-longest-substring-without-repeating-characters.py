class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = len(s)
        i = 0
        ans = -1
        l = 0
        d = {}
        if L==0:
            return 0
        
        for j in range(L):
            #print('---------------')
            #print('j : ', j)
            if s[j] not in d :
                #print('add : ', s[j])
                d[s[j]] = j
                l += 1
            elif s[j] in d :
                #print('already : ', s[j])
                prev = d[s[j]]
                while (i<j and d[s[i]] != prev):
                    #print('remove :', s[i])
                    del d[s[i]]
                    l -= 1
                    i+=1
                #print('remove :', s[i])
                del d[s[i]]
                l -= 1
                i+=1

                d[s[j]] = j
                l += 1
            ans = max(ans, l)

        return ans