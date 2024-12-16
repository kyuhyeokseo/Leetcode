class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def get_key(x):
            return str(x)
        
        L = list(range(1, n+1))
        L.sort(key = get_key)
        
        return L