class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        ret = []

        for i in range(len(asteroids)):
            curr = asteroids[i]

            while curr and ret:
                last = ret.pop()
                if last < 0:
                    ret.append(last)
                    break
                else:
                    if curr > 0:
                        ret.append(last)
                        break
                    else:
                        if last + curr > 0:
                            curr = last
                        elif last + curr < 0:
                            pass
                        else:
                            curr = 0

            if curr:
                ret.append(curr)

        return ret



