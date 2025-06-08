class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        ret = 0
        can = 0
        first = True

        for f in flowerbed:

            if f == 1 and first:
                if can > 0:
                    ret += (can // 2)
                can = 0
                first = False

            elif f == 1 and not first:
                if can > 0:
                    ret += ((can-1) // 2)
                can = 0

            else :
                can += 1

        if not first:
            ret += (can//2)
        else:
            if can > 0:
                ret += ((can+1)//2)

        return ret >= n