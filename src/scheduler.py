import heapq


class Scheduler:

    def __init__(self, tasks):

        self.tasks = tasks

    def optimize_schedule(self):

        completed = []
        missed = []

        current_time = 0
        total_profit = 0

        heap = []

        for idx, task in enumerate(self.tasks):

            score = (
                task.priority * 5
                + task.profit
                - task.execution_time
            )

            heapq.heappush(
                heap,
                (
                    -score,
                    task.deadline,
                    idx,
                    task
                )
            )

        while heap:

            _, _, _, task = heapq.heappop(heap)

            if (
                current_time
                + task.execution_time
                <= task.deadline
            ):

                completed.append(task)

                print(
                    f"Time {current_time}"
                    f" -> "
                    f"{current_time + task.execution_time}"
                    f" : {task.name}"
                )

                current_time += (
                    task.execution_time
                )

                total_profit += (
                    task.profit
                )

            else:

                missed.append(task)

        return (
            completed,
            missed,
            total_profit
        )