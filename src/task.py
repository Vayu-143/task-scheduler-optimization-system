class Task:

    def __init__(
        self,
        name,
        priority,
        deadline,
        execution_time,
        profit,
        depends_on=""
    ):

        self.name = name
        self.priority = int(priority)
        self.deadline = int(deadline)
        self.execution_time = int(execution_time)
        self.profit = int(profit)
        self.depends_on = depends_on

    def __repr__(self):

        return (
            f"{self.name}"
            f" | Priority={self.priority}"
            f" | Deadline={self.deadline}"
            f" | Time={self.execution_time}"
            f" | Profit={self.profit}"
        )