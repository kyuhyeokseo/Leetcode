class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num_list = list(map(int, str(num)))
        q = []
        ret = ''
        D_max = {}

        for i, n in enumerate(num_list):
            heapq.heappush(q, (-n, -i))
            D_max[n] = i
        
        for i in range(len(num_list)):
            t = heapq.heappop(q)
            N, I = -t[0], -t[1]

            if num_list[i] == N:
                ret += str(N)
            else:
                ret += str(N)
                num_list[D_max[N]] = num_list[i]

                for j in range(i+1, len(num_list)):
                    ret += str(num_list[j])
                return int(ret)
        return int(ret)