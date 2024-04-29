class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        d = {}
        l = len(words[0])
        ans = []
        for w in words:
            if w in d:
                d[w] += 1
            else :
                d[w] = 1

        for start in range(len(s)-l*len(words)+1):
            #print('------------------')
            check = {}
            tmp = 0
            target = s[start + tmp : start + tmp + l]
            while (d!=check and target in d):
                if target in check:
                    check[target] += 1
                else :
                    check[target] = 1

                #print(target, check)

                if check[target] > d[target] :
                    break

                tmp += l
                if start + tmp + l > len(s):
                    break
                else :
                    target = s[start + tmp : start + tmp + l]
            
            if check == d:
                ans.append(start)
            
        return ans
        
        
        