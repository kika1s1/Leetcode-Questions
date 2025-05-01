class Solution:
    def maxTaskAssign(
        self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def can_assign(count):
            remaining_pills = pills
            eligible_workers = deque()
            worker_index = m - 1

            for task_index in range(count - 1, -1, -1):
                difficulty = tasks[task_index]

                while worker_index >= m - count and workers[worker_index] + strength >= difficulty:
                    eligible_workers.appendleft(workers[worker_index])
                    worker_index -= 1

                if not eligible_workers:
                    return False

                if eligible_workers[-1] >= difficulty:
                    eligible_workers.pop()
                else:
                    if remaining_pills == 0:
                        return False
                    remaining_pills -= 1
                    eligible_workers.popleft()

            return True

        low, high, best = 1, min(n, m), 0
        while low <= high:
            mid = (low + high) // 2
            if can_assign(mid):
                best = mid
                low = mid + 1
            else:
                high = mid - 1

        return best
