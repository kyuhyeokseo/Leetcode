class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        self.D = {}
        self.D_all = {}

        for w in words :
            self.D[w] = True
            self.D_all[w] = True
        
        ret = []

        for w in words :
            for i in range(len(w)-1):
                w1, w2 = w[:i+1], w[i+1:]

                if w1 in self.D and w2 in self.D:
                    ret.append(w)
                    self.D[w] = True
                    self.D_all[w] = True
                    break

                if w1 in self.D and self.SubstringInD(w2):
                    ret.append(w)
                    self.D[w] = True
                    self.D_all[w] = True
                    break

        return ret
    
    def SubstringInD(self, w):

        if w in self.D_all :
            return self.D_all[w]
        
        for i in range(len(w)-1):
            w1, w2 = w[:i+1], w[i+1:]

            if w1 in self.D and w2 in self.D:
                self.D[w] = True
                self.D_all[w] = True
                return True

            if w1 in self.D and self.SubstringInD(w2):
                self.D[w] = True
                self.D_all[w] = True
                return True
        
        self.D_all[w] = False
        return False
