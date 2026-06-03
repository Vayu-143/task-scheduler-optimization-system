import pandas as pd


def generate_report(
        completed,
        missed,
        total_profit
):

    print("\n==========================")
    print("OPTIMIZED TASK SCHEDULE")
    print("==========================")

    for task in completed:
        print(task)

    print("\n==========================")
    print("MISSED TASKS")
    print("==========================")

    for task in missed:
        print(task)

    print("\n==========================")
    print("TOTAL PROFIT")
    print("==========================")

    print(total_profit)

    report = []

    for task in completed:
        report.append(
            [
                task.name,
                "Completed",
                task.priority,
                task.deadline,
                task.execution_time,
                task.profit
            ]
        )

    for task in missed:
        report.append(
            [
                task.name,
                "Missed",
                task.priority,
                task.deadline,
                task.execution_time,
                task.profit
            ]
        )

    df = pd.DataFrame(
        report,
        columns=[
            "Task",
            "Status",
            "Priority",
            "Deadline",
            "Execution Time",
            "Profit"
        ]
    )

    df.to_csv(
        "outputs/schedule_report.csv",
        index=False
    )

    with open(
            "outputs/schedule_report.txt",
            "w"
    ) as file:

        file.write(
            f"Total Profit: {total_profit}\n"
        )

        file.write("\nCompleted Tasks\n")

        for task in completed:
            file.write(f"{task}\n")

        file.write("\nMissed Tasks\n")

        for task in missed:
            file.write(f"{task}\n")