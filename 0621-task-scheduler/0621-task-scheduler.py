from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = Counter(tasks).most_common()
        
        ret = (n+1) * (counter[0][1] - 1) + 1
        MAX = counter[0][1]
        avs = n * (counter[0][1] - 1)

        if len(counter) == 0:
            return ret

        for c in counter[1:]:
            item, cnt = c[0], c[1]
            if cnt == MAX:
                avs -= (MAX-1)
                ret += 1
                if avs < 0:
                    ret += (-avs)
                    avs = 0
            else:
                avs -= cnt
                if avs < 0:
                    ret += (-avs)
                    avs = 0
            
        return ret
