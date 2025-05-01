from sortedcontainers import SortedList
class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.userid_to_task = defaultdict(dict)  
        self.task_to_user = {}  
        self.order_with_priority = SortedList()  
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        
        self.userid_to_task[userId][taskId] = priority
        
        self.task_to_user[taskId] = userId
        
        self.order_with_priority.add((-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        
        userId = self.task_to_user[taskId]
        current_priority = self.userid_to_task[userId][taskId]
        
        self.order_with_priority.remove((-current_priority, -taskId, userId))
        
        self.userid_to_task[userId][taskId] = newPriority
        
        self.order_with_priority.add((-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        
        userId = self.task_to_user[taskId]
        priority = self.userid_to_task[userId][taskId]
        
        del self.userid_to_task[userId][taskId]
        
        self.order_with_priority.remove((-priority, -taskId, userId))
        
        del self.task_to_user[taskId]

    def execTop(self) -> int:
        if not self.order_with_priority:
            return -1  
        
        priority, taskId, userId = self.order_with_priority.pop(0)
        taskId = -taskId  
        
        del self.userid_to_task[userId][taskId]
        
        del self.task_to_user[taskId]
        return userId

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()