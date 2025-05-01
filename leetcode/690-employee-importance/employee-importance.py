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
        total = 0
        stack = []
        stack.append(id)
        while stack:
            new_id = stack.pop()

            for i in range(len(employees)):
                if employees[i].id == new_id:
                    total +=employees[i].importance
                    for i in employees[i].subordinates:
                        stack.append(i)
        # print(employees[1].id)
        return total
        
        

        