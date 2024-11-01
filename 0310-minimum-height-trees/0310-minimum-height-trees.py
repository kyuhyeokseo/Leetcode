class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1 :
            return [0]
        
        N = n
        E = [[] for _ in range(n)]
        deg = [0 for _ in range(n)]
        
        for item in edges :
            x,y = item[0], item[1]
            E[x].append(y)
            E[y].append(x)
            deg[x] += 1
            deg[y] += 1
        
        leaf = []
        for i in range(n):
            if deg[i] == 1 :
                leaf.append(i)
                
        while N > 2 :
            
            N -= len(leaf)
            
            tmp = []
            
            for l in leaf :
                
                for adj in E[l]:
                    deg[adj] -= 1
                    if deg[adj] == 1 :
                        tmp.append(adj)
            
            leaf = tmp[:]
        
        return leaf
        