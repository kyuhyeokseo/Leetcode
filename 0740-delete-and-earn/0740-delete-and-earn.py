class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        D = {}
        for n in nums:
            if n in D:
                D[n] += n
            else:
                D[n] = n
        
        n_list = sorted(list(D.keys()))
        tmp = [0, 0]

        for i, n in enumerate(n_list):
            if i > 0 and n_list[i-1] + 1 == n:
                tmp = [tmp[1] + D[n], max(tmp[0], tmp[1])]
            else:
                tmp = [max(tmp[0], tmp[1]) + D[n], max(tmp[0], tmp[1])]

        return max(tmp)