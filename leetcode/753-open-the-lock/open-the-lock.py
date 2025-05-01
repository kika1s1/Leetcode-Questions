class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        next_slot = {
            "0": "1",
            "1": "2",
            "2": "3",
            "3": "4",
            "4": "5",
            "5": "6",
            "6": "7",
            "7": "8",
            "8": "9",
            "9": "0",
        }
        prev_slot = {
            "0": "9",
            "1": "0",
            "2": "1",
            "3": "2",
            "4": "3",
            "5": "4",
            "6": "5",
            "7": "6",
            "8": "7",
            "9": "8",
        }

        visited_combinations = set(deadends)
        pending_combinations = deque()

        turns = 0

        if "0000" in visited_combinations:
            return -1

        pending_combinations.append("0000")
        visited_combinations.add("0000")

        while pending_combinations:
            curr_level_nodes_count = len(pending_combinations)
            for _ in range(curr_level_nodes_count):
                current_combination = pending_combinations.popleft()

                
                if current_combination == target:
                    return turns

                
                for wheel in range(4):
                    
                    new_combination = list(current_combination)
                    new_combination[wheel] = next_slot[new_combination[wheel]]
                    new_combination_str = "".join(new_combination)
                   
                    if new_combination_str not in visited_combinations:
                        pending_combinations.append(new_combination_str)
                        visited_combinations.add(new_combination_str)

                    
                    new_combination = list(current_combination)
                    new_combination[wheel] = prev_slot[new_combination[wheel]]
                    new_combination_str = "".join(new_combination)
        
                    if new_combination_str not in visited_combinations:
                        pending_combinations.append(new_combination_str)
                        visited_combinations.add(new_combination_str)

            turns += 1

        return -1