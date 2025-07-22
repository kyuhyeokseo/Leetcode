from fractions import Fraction

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
    
        cards__ = []
        for i in range(4):
            cards__.append(Fraction(cards[i]))

        for i in range(4):
            cards_cpy = cards__[:]
            cards_cpy.pop(i)
            result = self.dfs([cards[i]], cards_cpy)
            if result:
                return result
        
        for (a,b,c,d) in [(0,1,2,3), (0,2,1,3), (0,3,1,2)]:
            s1 = set()
            s1.add(cards[a] + cards[b])
            s1.add(cards[a] * cards[b])
            s1.add(cards[a] - cards[b])
            s1.add(cards[a] / cards[b])
            s1.add(cards[b] - cards[a])
            s1.add(cards[b] / cards[a])

            s2 = set()
            s2.add(cards[c] + cards[d])
            s2.add(cards[c] * cards[d])
            s2.add(cards[c] - cards[d])
            s2.add(cards[c] / cards[d])
            s2.add(cards[d] - cards[c])
            s2.add(cards[d] / cards[c])

            for v1 in list(s1):
                for v2 in list(s2):
                    if v1+v2==24 or v1-v2==24 or v2-v1==24 or v1*v2==24 or (v1 and v2/v1==24) or (v2 and v1/v2==24):
                        return True

        return False
    
    def dfs(self, values, cards):

        #print(f'----- VALUE: {values},  CARD: {cards} -----')

        L = len(cards)

        for i in range(L):
            new_values = set()
            cards_cpy = cards[:]
            n = cards[i]

            for v in values:

                #print(f'CARD {n}, VALUE {v}')
                new_values.add(n+v)
                new_values.add(n*v)
                new_values.add(n-v)
                new_values.add(v-n)
                if v:
                    new_values.add(n/v)
                if n:
                    new_values.add(v/n)
        
            if L == 1:
                for v in new_values:
                    if v == 24:
                        return True
                return False
            
            cards_cpy.pop(i)
            if self.dfs(list(new_values), cards_cpy):
                return True
        
        return False


        

