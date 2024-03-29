class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        N = len(ratings)
        tmp = []
        move = 0
        step = 0
        
        if N==1 :
            return 1
        else :
            for n in range(1,N,1):
                if ratings[n] > ratings[n-1] :
                    if move == 1:
                        step += 1
                    elif move == 0:
                        tmp.append((0, step))
                        step = 1
                        move = 1
                    else :
                        tmp.append((-1, step))
                        step = 1
                        move = 1
                elif ratings[n] == ratings[n-1] :
                    if move == 1:
                        tmp.append((1, step))
                        step = 1
                        move = 0
                    elif move == 0:
                        step += 1
                    else :
                        tmp.append((-1, step))
                        step = 1
                        move = 0
                if ratings[n] < ratings[n-1] :
                    if move == 1:
                        tmp.append((1, step))
                        step = 1
                        move = -1
                    elif move == 0:
                        tmp.append((0, step))
                        step = 1
                        move = -1
                    else :
                        step += 1

            tmp.append((move, step))  
            if tmp[0][1] == 0 :
                tmp[:] = tmp[1:]    

            if len(tmp) == 1:
                m, s = tmp[0]
                if m == 0:
                    return s+1
                else :
                    return (s+1) * (s+2) // 2

            sum = 0
            for idx in range(len(tmp)-1):
                m1, s1 = tmp[idx]
                m2, s2 = tmp[idx+1]
                if idx == 0:
                    if m1 >= 0 :
                        sum += 1
                    else :
                        sum += (s1 +1)


                if m1 == 1 and m2 == 0 :
                    sum += ((s1+1) * (s1+2) // 2 - 1)
                elif m1 == 1 and m2 == -1 :
                    sum += ((s1 * (s1+1))//2 + max(s1, s2))
                elif m1 == 0 and m2 >= 0:
                    sum += s1
                elif m1 == 0 and m2 == -1:
                    sum += s1 + s2
                elif m1 == -1 :
                    sum += (s1 * (s1+1) // 2)
                    
                #print(sum)
            
            m, s = tmp[len(tmp)-1]
            if m == 1 :
                sum += ((s+1) * (s+2) // 2 - 1)
            elif m == 0:
                sum += s
            elif m == -1 : 
                sum += (s * (s+1) // 2)
            #print(sum)

            return sum
