class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        N = len(nums)
        visited = [False] * N

        for idx in range(N):
            if visited[idx] :
                continue
            
            #print(f'--- START INDEX : {idx} ---')

            curr = idx
            flag = 1 if nums[curr] > 0 else -1
            S = set()

            while True :
                nxt = (curr + nums[curr]) % N
                test_flag = 1 if nums[curr] > 0 else -1

                #print(f'curr : {curr}, nxt : {nxt}')
                if visited[nxt] and not(nxt in S) :
                    break
                elif curr == nxt :
                    break
                elif flag != test_flag :
                    break
                elif curr != nxt and visited[nxt] and (nxt in S) and flag == test_flag :
                    return True

                visited[curr] = True
                S.add(curr)
                curr = nxt
                #print(visited, S)
        
        return False
                