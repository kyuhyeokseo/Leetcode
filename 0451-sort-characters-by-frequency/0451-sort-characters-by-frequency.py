import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        
        D = {}

        for t in s :
            if t in D :
                D[t] += 1
            else :
                D[t] = 1

        q = []
        for (c, cnt) in D.items():
            q.append((-cnt, c))
        heapq.heapify(q)

        result = ''
        while q :
            n, c = heapq.heappop(q)
            n *= -1
            result += c*n
        
        return result

