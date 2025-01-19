import heapq

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        q = []
        for i, interval in enumerate(intervals) :
            srt = interval[0]
            end = interval[1]
            heapq.heappush(q, [srt, 1, i, 's'])
            heapq.heappush(q, [end, 0, i, 'e'])
        
        ret = [-1 for _ in range(len(intervals))]
        stk = []

        while q :
            val, _, idx, flag = heapq.heappop(q)
            if flag == 'e':
                stk.append(idx)
            else :
                while stk :
                    i = stk.pop()
                    ret[i] = idx
            #print('-' * 10)
            #print(val, idx, flag)
            #print(stk)
            #print(ret)
        
        return ret
