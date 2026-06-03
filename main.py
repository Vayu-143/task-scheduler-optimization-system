from src.utils import load_tasks
from src.scheduler import Scheduler
from src.dependency_scheduler import DependencyScheduler
from src.report_generator import generate_report
from src.gantt_chart import create_gantt_chart
from src.metrics import calculate_metrics


def main():

    print("\n===================================")
    print("TASK SCHEDULER OPTIMIZATION SYSTEM")
    print("===================================\n")

    # Load Tasks
    tasks = load_tasks("data/tasks.csv")

    print(f"Loaded {len(tasks)} tasks successfully.\n")

    # Apply Dependency Scheduling (Topological Sort)
    dependency_scheduler = DependencyScheduler(tasks)

    tasks = dependency_scheduler.topological_sort()

    print("Task Dependency Resolution Completed.\n")

    # Run Priority Queue Scheduler
    scheduler = Scheduler(tasks)

    completed, missed, total_profit = (
        scheduler.optimize_schedule()
    )

    # Generate Reports
    generate_report(
        completed,
        missed,
        total_profit
    )

    # Generate Gantt Chart
    create_gantt_chart(completed)

    print("\nGantt Chart Generated:")
    print("outputs/gantt_chart.png")

    # Performance Metrics
    metrics = calculate_metrics(
        completed,
        missed,
        total_profit
    )

    print("\n==========================")
    print("PERFORMANCE METRICS")
    print("==========================")

    for key, value in metrics.items():
        print(f"{key}: {value}")

    print("\n==========================")
    print("COMPLETED TASKS")
    print("==========================")

    for task in completed:
        print(task)

    print("\n==========================")
    print("MISSED TASKS")
    print("==========================")

    for task in missed:
        print(task)

    print("\n==========================")
    print("PROJECT EXECUTION SUCCESS")
    print("==========================")

    print("CSV Report Saved")
    print("TXT Report Saved")
    print("Gantt Chart Saved")
    print("Dashboard Ready")


if __name__ == "__main__":
    main()