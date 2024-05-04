class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        
        points.sort()
        #print(points)
        #print("-----------------")

        cnt = 0
        target_idx = 0
        L = len(points)
        while(target_idx < L):
            
            tX, tY = points[target_idx]

            tmp_idx = target_idx + 1
            remove_list = []
            if tmp_idx >= L :
                cnt += 1
                return cnt

            while (points[tmp_idx][0] <= tY):
                remove_list.append(points[tmp_idx])
                tY = min(tY, points[tmp_idx][1])
                tmp_idx += 1
                if tmp_idx >= L :
                    cnt += 1
                    return cnt
            
            cnt += 1    
            target_idx = tmp_idx

            #print(remove_list)
            #print(tmp_idx)
            #print(points[tmp_idx])
            #print('--------------------')

        return points

        
        
        
        