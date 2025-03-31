class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        
        S = 0
        for m in machines:
            S += m

        avg, rem = S // len(machines), S % len(machines)
        if rem > 0:
            return -1

        machines = [m - avg for m in machines]

        MAX = max(machines)
        CUM = max(map(abs, accumulate(machines)))
        return max(MAX, CUM)
