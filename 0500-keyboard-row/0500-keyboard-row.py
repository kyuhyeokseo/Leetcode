class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f,s,t = "qwertyuiop", "asdfghjkl", "zxcvbnm"
        D = {}
        for i, row in enumerate([f,s,t]):
            for s in row:
                D[s.lower()] = i
        
        ret = []
        for word in words:
            val = D[word[0].lower()]
            for s in word:
                if val != D[s.lower()]:
                    val = -1
                    break
            if val >= 0:
                ret.append(word)
        
        return ret