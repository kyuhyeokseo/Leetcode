class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        lasts = defaultdict(list)

        for n in nums:
            if lasts[n-1]:
                heappush(lasts[n], heappop(lasts[n-1]) + 1)
            else:
                heappush(lasts[n], 1)
        
        return all(
            cnt >= 3
            for D in lasts.values()
            for cnt in D
        )