import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        currT, HQ = 0, []

        courses = sorted(courses, key=lambda x: x[1])
        #print(courses)

        for course in courses:
            T,L = course[0], course[1]
            if currT + T <= L:
                currT += T
                heapq.heappush(HQ, -T)
            else:
                if HQ:
                    M = - heapq.heappop(HQ)
                    if M > T:
                        currT += (T-M)
                        heapq.heappush(HQ, -T)
                    else:
                        heapq.heappush(HQ, -M)
            #print(currT, HQ)
        
        return len(HQ)