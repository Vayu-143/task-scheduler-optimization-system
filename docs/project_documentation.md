# Task Scheduler Optimization System

## Project Overview

The Task Scheduler Optimization System is a DSA-based project that schedules tasks efficiently using Priority Queue and Greedy Algorithms.

The objective is to maximize completed tasks and profit while minimizing missed deadlines.

---

# Problem Statement

Organizations handle multiple tasks with:

- Different priorities
- Deadlines
- Execution durations
- Business value

Poor scheduling can result in:

- Missed deadlines
- Reduced productivity
- Financial losses

This project solves the problem by generating an optimized execution sequence.

---

# Workflow

```text
Task Input
    │
    ▼
Task Validation
    │
    ▼
Priority Queue
    │
    ▼
Greedy Scheduling
    │
    ▼
Optimized Task Order
    │
    ▼
Performance Analysis
    │
    ▼
Reports & Visualization
```

---

# DSA Concepts Used

## Sorting

Used for task organization.

Complexity:

```text
O(n log n)
```

---

## Heap

Used for efficient priority management.

Operations:

```text
Insert : O(log n)
Delete : O(log n)
```

---

## Priority Queue

Ensures higher-priority tasks are processed first.

---

## Greedy Algorithm

Makes locally optimal scheduling decisions.

---

# Features

- CSV Task Input
- Task Validation
- Priority Queue Scheduling
- Heap Operations
- Deadline Handling
- Profit Optimization
- Missed Task Detection
- CSV Reports
- TXT Reports
- Gantt Chart Visualization
- Performance Metrics

---

# Input Parameters

| Parameter | Description |
|------------|------------|
| Task | Task Name |
| Priority | Task Importance |
| Deadline | Completion Deadline |
| Execution Time | Duration |
| Profit | Value Generated |

---

# Outputs

## Schedule Report

Generated:

```text
outputs/schedule_report.txt
```

---

## CSV Report

Generated:

```text
outputs/schedule_report.csv
```

---

## Gantt Chart

Generated:

```text
outputs/gantt_chart.png
```

---

# Performance Metrics

Generated Metrics:

- Total Tasks
- Completed Tasks
- Missed Tasks
- Completion Rate
- Total Profit

---

# Technologies Used

## Programming Language

Python

---

## Libraries

- Pandas
- Matplotlib
- Streamlit

---

# Folder Structure

```text
Task-Scheduler-Optimization-System
│
├── data
├── docs
├── images
├── outputs
├── src
│
├── main.py
├── dashboard.py
├── requirements.txt
└── README.md
```

---

# Future Enhancements

## Multi-Core Scheduling

Support multiple workers.

---

## Task Dependencies

Implement:

- Graph
- DAG
- Topological Sort

---

## Database Integration

Replace CSV with:

- SQLite
- PostgreSQL

---

## REST API

Implement:

- Flask
- FastAPI

---

# Learning Outcomes

Through this project:

- Heap operations were implemented.
- Priority Queues were used practically.
- Scheduling algorithms were explored.
- Greedy optimization was applied.
- Visualization and reporting were integrated.

This project demonstrates industry-relevant Data Structures and Algorithms concepts applicable in Operating Systems, Project Management Tools, Cloud Scheduling Systems, and Backend Development.