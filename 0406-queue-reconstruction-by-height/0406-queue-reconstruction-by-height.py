import heapq
from collections import defaultdict

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        ret = []
        q = []
        d = defaultdict(list)

        for i, p in enumerate(people):
            if p[1] == 0 :
                heapq.heappush(q, (p[0], i))
            else :
                d[p[0]].append([p[1], i])
        
        #print(q)
        #print(d)

        while q :
            out = heapq.heappop(q)
            H, idx = out[0], out[1]

            ret.append(people[idx])

            for k in d.keys():

                if H >= k :
                    k_list = d[k]

                    for item in k_list :
                        item[0] -= 1
                        if item[0] == 0 :
                            heappush(q, (people[item[1]][0], item[1]))
                    
                    for item in k_list :
                        if item[0] == 0 :
                            k_list.remove(item)

            #print(q)
            #print(d)

        
        return ret




