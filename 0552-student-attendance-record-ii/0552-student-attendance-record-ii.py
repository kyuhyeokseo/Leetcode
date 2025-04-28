class Solution:
    def checkRecord(self, n: int) -> int:
        
        VAL = 10 ** 9 + 7

        #update : A0L0, A1L0, A0L1, A1L1, A0L2, A1L2
        update = [0 for _ in range(6)]
        tmp = [0 for _ in range(6)]

        update = [1, 1, 1, 0, 0, 0]

        for _ in range(n-1):
            tmp[0] = (update[0] + update[2] + update[4]) % VAL
            tmp[1] = (update[0] + update[1] + update[2] + update[3] + update[4] + update[5]) % VAL
            tmp[2] = update[0]
            tmp[3] = update[1]
            tmp[4] = update[2]
            tmp[5] = update[3]
            for i in range(6):
                update[i] = tmp[i]
            #print(update)
        
        return sum(update) % VAL