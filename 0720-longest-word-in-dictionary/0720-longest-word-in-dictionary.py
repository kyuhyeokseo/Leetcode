class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        rec = {}
        words = sorted(words, reverse=True)
        words = sorted(words, key=len)  
        ret = ""

        for w in words:
            if len(w) == 1:
                rec[w] = True
                ret = w
            else:
                if w[:-1] in rec:
                    rec[w] = True
                    ret = w
        
        return ret
        
        