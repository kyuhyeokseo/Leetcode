import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        ans = []
        X = 0
        D_in, D_out = defaultdict(list), defaultdict(list)
        x_list = []
        
        for item in buildings :
            srt, end, h = item[0], item[1], item[2]
            
            D_in[srt].append(h)
            D_out[end].append(h)
            x_list.append(srt)
            x_list.append(end)
        
            X = max(X, item[1])
        
        q = [0]
        H = 0
        
        x_list = list(set(x_list))
        x_list.sort()

        for i in x_list:
            
            if i in D_in :
                for item in D_in[i] :
                    heapq.heappush(q, -item)
            
            if i in D_out :
                for item in D_out[i]:
                    q.remove(-item)
            
            heapq.heapify(q)
            H_new = -q[0]
            
            if H_new != H :
                H = H_new
                ans.append([i, H_new])
        
        return ans
        
        
        
        