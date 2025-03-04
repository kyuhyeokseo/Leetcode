class Solution:
    def magicalString(self, n: int) -> int:
        
        s_list = [1,2,2,1,1,2]
        cnt = [1,2,2,1]

        if n < 6 :
            a = [1,1,1,2,3]
            return a[n-1]

        s_len = 6
        ret = 3

        while s_len < n :
            #print(s_list, cnt)
            L = len(cnt)
            while len(cnt) < len(s_list):
                idx = len(cnt)
                cnt.append(s_list[idx])
            
            N = 2 if s_list[-1] == 1 else 1
            for i in range(L, len(cnt)):
                C = cnt[i]
                for _ in range(C):
                    s_list.append(N)
                    s_len += 1
                    if N == 1 :
                        ret += 1
                    if s_len == n :
                        return ret
                N = 1 if s_list[-1] == 2 else 2

        #print(s_list, cnt)
        return ret