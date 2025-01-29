class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        cnt = 0
        L = len(nums)

        D = {}

        if L < 3 :
            return 0

        for j_idx in range(1, L):

            j = nums[j_idx]

            if j in D :
                prev_dict = D[j]
                prev_list = list(D[j].keys())[:]

                for prev in prev_list :
                    cnt += D[j][prev]
                    diff = j - prev
                    nxt = j + diff
                    if nxt in D :
                        if j in D[nxt]:
                            D[nxt][j] += D[j][prev]
                        else :
                            D[nxt][j] = D[j][prev]
                    else :
                        D[nxt] = {}
                        D[nxt][j] = D[j][prev]

            for i_idx in range(j_idx):

                i = nums[i_idx]

                diff = j-i
                key = j + diff
                if key in D :
                    if j in D[key]:
                        D[key][j] += 1
                    else :
                        D[key][j] = 1
                else :
                    D[key] = {}
                    D[key][j] = 1
        
        return cnt