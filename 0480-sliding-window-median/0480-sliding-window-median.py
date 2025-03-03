import heapq

class Solution:

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        def getMedian(maxQ, minQ):
            if k % 2 == 0 :
                return (minQ[0] - maxQ[0]) / 2
            else :
                return minQ[0]

        ret = []

        MAX_q, MIN_q = [], []

        rec = defaultdict(int)

        for idx in range(k):
            heapq.heappush(MAX_q, -nums[idx])
            if len(MAX_q) > int(k//2):
                heapq.heappush(MIN_q, -heapq.heappop(MAX_q))

        M = getMedian(MAX_q, MIN_q)
        ret.append(M)

        print(MAX_q, MIN_q, M)

        for idx in range(len(nums) - k):
            rem, add = nums[idx], nums[k+idx]

            rec[rem] += 1

            balance = 0
            if rem < M :
                balance -= 1
            else :
                balance += 1
            
            if add < M :
                balance += 1
                heapq.heappush(MAX_q, -add)
            else :
                balance -= 1
                heapq.heappush(MIN_q, add)
            
            if balance > 0 :
                heapq.heappush(MIN_q, -heapq.heappop(MAX_q))
            elif balance < 0 :
                heapq.heappush(MAX_q, -heapq.heappop(MIN_q))
            
            while MIN_q and rec[MIN_q[0]] > 0 :
                rec[MIN_q[0]] -= 1
                heapq.heappop(MIN_q)

            while MAX_q and rec[-MAX_q[0]] > 0 :
                rec[-MAX_q[0]] -= 1
                heapq.heappop(MAX_q)
            
            #print('LINE 60 ', MAX_q, MIN_q)
            M = getMedian(MAX_q, MIN_q)
            ret.append(M)

            #print(MAX_q, MIN_q, M)
        
        return ret
