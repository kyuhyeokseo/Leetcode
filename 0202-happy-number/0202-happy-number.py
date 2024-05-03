class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        cnt = 0
        while (n!=1 and n not in d):
            #print(n)
            d[n] = 1
            n = self.getNext(n)
            cnt += 1

        if n == 1 :
            return True
        else :
            return False
        

    def getNext(self, x) :
        tmp = 0
        while (x != 0):
            tmp += (x%10) ** 2
            x = x//10
        return tmp