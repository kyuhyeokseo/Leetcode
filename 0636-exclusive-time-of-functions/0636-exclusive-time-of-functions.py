class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        N = n
        ret, stack = [0 for _ in range(N)], []
        off_logs = []
        
        for log in logs:
            tmp = log.split(':')
            f_id, flag, t = int(tmp[0]), tmp[1], int(tmp[2])

            if flag == 'start':
                if stack:
                    F_id, T = stack[-1][0], stack[-1][1]
                    stack.pop()
                    ret[F_id] += (t-T)
                    off_logs.append([F_id, f_id])
                stack.append((f_id, t))
            else:
                F_id, T = stack[-1][0], stack[-1][1]
                stack.pop()
                if F_id == f_id:
                    ret[F_id] += (t-T+1)
                if off_logs:
                    re_id = off_logs.pop()[0]
                    stack.append((re_id, t+1))

            #print(ret, stack)
        
        return ret