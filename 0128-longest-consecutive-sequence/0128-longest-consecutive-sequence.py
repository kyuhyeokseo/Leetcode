class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        d = {}
        check = {}
        for num in nums :
            #print(f'======= {num} ========')
            if num in check :
                continue
            
            check[num] = True
            if (num - 1, 1) in d and (num + 1, -1) in d :
                cnt1 = d[(num -1,  1)]
                cnt2 = d[(num +1, -1)]
                cnt = cnt1 + cnt2 + 1
                d[(num - cnt1, -1)] = cnt
                d[(num + cnt2,  1)] = cnt
                del d[(num -1,  1)]
                del d[(num +1, -1)]
                #print(d[(num - cnt1, -1)], d[(num + cnt2,  1)])

            elif (num - 1, 1) in d :
                cnt = d[(num-1,1)]
                d[(num, 1)] = cnt + 1
                d[(num-cnt, -1)] = cnt + 1
                del d[(num-1, 1)]
                #print(d[(num, 1)])
            
            elif (num + 1, -1) in d :
                cnt = d[(num +1, -1)]
                d[(num , -1)] = cnt + 1
                d[(num + cnt, 1)] = cnt + 1
                del d[(num +1, -1)]
                #print(d[(num, -1)])
            
            else :
                d[(num, 1)] = 1
                d[(num, -1)] = 1
                #print(d[(num, 1)])
                #print(d[(num, -1)])
        
            #print(d)

        #print("------------------------")
        ans = 0
        for v in d.values():
            ans = max(ans, v)
        
        return ans