# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        self.X = []
        self.idx = 0
        
        def is_only_integer(y):
            
            flg = True
            out = []
            
            for item in y :
                
                if item.isInteger():
                    out.append(item)
                else :
                    flg = False
                    L = item.getList()
                    for z in L :
                        out.append(z)
                        
            return out, flg
    
        
        out, flag = is_only_integer(nestedList)

        if flag is False :
            while flag is False :
                out, flag = is_only_integer(out)
        
        for item in out :
            self.X.append(item.getInteger())
        
        self.L = len(self.X)
        
    
    def next(self) -> int:
        
        if self.idx < self.L :
            self.idx += 1
            return self.X[self.idx-1]

    
    def hasNext(self) -> bool:
        return self.idx < self.L
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())