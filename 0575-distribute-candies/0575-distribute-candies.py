class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        N = len(candyType)
        S = set()

        for candy in candyType:
            S.add(candy)
        
        return min(N//2, len(S))