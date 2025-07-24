class Solution:

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        
        N = len(edges)
        parents = [i for i in range(N+1)]
        e1, e2 = None, None

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False
            parents[rootY] = rootX
            return True
        

        for p, c in edges:
            if parents[c] != c:
                e1 = [parents[c], c]
                e2 = [p, c]
            else:
                parents[c] = p
        
        parents = [i for i in range(N+1)]

        for p, c in edges:
            if [p, c] == e2:
                continue
            if not union(p, c):
                if e1:
                    return e1
                return [p, c]
        
        return e2
