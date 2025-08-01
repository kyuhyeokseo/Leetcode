class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        D = {}
        for w in words:
            if w in D:
                D[w] += 1
            else:
                D[w] = 1
        
        ret = []
        for key in D.keys():
            ret.append((-D[key], key))
        
        ret.sort()
        ans = []
        for i in range(k):
            ans.append(ret[i][1])

        return ans