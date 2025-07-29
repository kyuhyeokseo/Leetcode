"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        ret = 0
        deq = collections.deque([id])
        EMP = {}

        for emp in employees:
            EMP[emp.id] = emp

        while deq:
            emp = EMP[deq.popleft()]
            ret += emp.importance
            for sub in emp.subordinates:
                deq.append(sub)
        
        return ret