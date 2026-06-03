import pandas as pd
from src.task import Task


def load_tasks(csv_path):
    df = pd.read_csv(csv_path)

    tasks = []

    for _, row in df.iterrows():
        task = Task(
            row["Task"],
            row["Priority"],
            row["Deadline"],
            row["ExecutionTime"],
            row["Profit"]
        )
        tasks.append(task)

    return tasks