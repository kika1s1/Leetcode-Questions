class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time_line = 0
        total_waiting_time = 0
        
        for arrival, prep_time in customers:
            if time_line < arrival:
                time_line = arrival
            time_line += prep_time
            total_waiting_time += time_line - arrival
        
        return total_waiting_time / len(customers)
