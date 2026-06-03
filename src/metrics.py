def calculate_metrics(
    completed,
    missed,
    total_profit
):

    total_tasks = len(completed) + len(missed)

    completion_rate = (
        len(completed) / total_tasks
    ) * 100

    metrics = {
        "Total Tasks": total_tasks,
        "Completed Tasks": len(completed),
        "Missed Tasks": len(missed),
        "Completion Rate": round(
            completion_rate,
            2
        ),
        "Total Profit": total_profit
    }

    return metrics