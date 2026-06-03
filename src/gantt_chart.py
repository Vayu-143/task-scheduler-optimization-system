import matplotlib.pyplot as plt


def create_gantt_chart(tasks):

    fig, ax = plt.subplots(figsize=(10, 5))

    current_time = 0

    for task in tasks:

        ax.barh(
            task.name,
            task.execution_time,
            left=current_time
        )

        current_time += task.execution_time

    ax.set_title("Task Schedule Timeline")
    ax.set_xlabel("Time")
    ax.set_ylabel("Tasks")

    plt.tight_layout()

    plt.savefig("outputs/gantt_chart.png")

    plt.close()