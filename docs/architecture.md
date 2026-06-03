# Task Scheduler Optimization System Architecture

## Overview

The system optimizes task execution order using Priority Queue and Greedy Scheduling techniques.

---

## Architecture Diagram

```text
                User
                  │
                  ▼
          tasks.csv Input
                  │
                  ▼
          Task Loader Module
                  │
                  ▼
          Task Object Creation
                  │
                  ▼
        Scheduler Engine
      (Heap + Priority Queue)
                  │
                  ▼
         Greedy Optimization
                  │
      ┌───────────┴───────────┐
      ▼                       ▼
Completed Tasks          Missed Tasks
      │                       │
      └───────────┬───────────┘
                  ▼
         Performance Metrics
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
CSV Report   TXT Report   Gantt Chart
                  │
                  ▼
          Streamlit Dashboard
```

---

## Components

### 1. Task Loader

Reads task information from CSV.

Input:

- Task Name
- Priority
- Deadline
- Execution Time
- Profit

Output:

- Task Objects

---

### 2. Scheduler Engine

Responsible for:

- Sorting tasks
- Heap operations
- Priority Queue management
- Scheduling optimization

Algorithms Used:

- Heap
- Priority Queue
- Greedy Scheduling

---

### 3. Report Generator

Generates:

- schedule_report.csv
- schedule_report.txt

---

### 4. Metrics Engine

Calculates:

- Total Tasks
- Completed Tasks
- Missed Tasks
- Completion Rate
- Total Profit

---

### 5. Gantt Chart Generator

Visualizes task execution timeline.

Output:

- gantt_chart.png

---

### 6. Dashboard

Displays:

- Reports
- Metrics
- Charts
- Schedule Overview

Technology:

- Streamlit
