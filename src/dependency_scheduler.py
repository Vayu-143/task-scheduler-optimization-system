from collections import defaultdict, deque


class DependencyScheduler:

    def __init__(self, tasks):

        self.tasks = tasks

    def topological_sort(self):

        graph = defaultdict(list)
        indegree = defaultdict(int)

        task_map = {}

        for task in self.tasks:

            task_map[task.name] = task

            if task.depends_on:

                graph[task.depends_on].append(
                    task.name
                )

                indegree[task.name] += 1

        queue = deque()

        for task in self.tasks:

            if indegree[task.name] == 0:
                queue.append(task.name)

        ordered = []

        while queue:

            current = queue.popleft()

            ordered.append(
                task_map[current]
            )

            for neighbor in graph[current]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:

                    queue.append(
                        neighbor
                    )

        return ordered