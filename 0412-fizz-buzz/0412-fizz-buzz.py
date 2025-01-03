class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        full = []

        for i in range(1, n+1):

            if i % 5 == 0 :
                if i % 3 == 0 :
                    full.append("FizzBuzz")
                else :
                    full.append("Buzz")
            else :
                if i % 3 == 0 :
                    full.append("Fizz")
                else :
                    full.append(str(i))
        
        return full
