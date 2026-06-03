import streamlit as st
import pandas as pd
import plotly.express as px
import networkx as nx
import matplotlib.pyplot as plt

# ------------------------------------
# PAGE CONFIG
# ------------------------------------

st.set_page_config(
    page_title="Task Scheduler Dashboard",
    page_icon="🚀",
    layout="wide"
)

# ------------------------------------
# HEADER
# ------------------------------------

st.title("🚀 Task Scheduler Optimization System")

st.markdown(
    """
    ### AI-Powered Task Scheduler

    Priority Queue • Heap • Topological Sort • Greedy Optimization
    """
)

st.info(
    """
    Scheduler Uses:

    • Priority Queue

    • Heap

    • Greedy Scheduling

    • Topological Sort

    • Dependency Graphs
    """
)

# ------------------------------------
# CSV UPLOAD
# ------------------------------------

uploaded_file = st.file_uploader(
    "Upload Task CSV",
    type=["csv"]
)

if uploaded_file:

    uploaded_df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Dataset")

    st.dataframe(uploaded_df)

# ------------------------------------
# LOAD REPORT
# ------------------------------------

df = pd.read_csv(
    "outputs/schedule_report.csv"
)

# ------------------------------------
# FILTERS
# ------------------------------------

st.subheader("📋 Schedule Report")

status_filter = st.selectbox(
    "Filter Tasks",
    [
        "All",
        "Completed",
        "Missed"
    ]
)

if status_filter != "All":

    filtered_df = df[
        df["Status"] == status_filter
    ]

else:

    filtered_df = df

st.dataframe(
    filtered_df,
    use_container_width=True
)

# ------------------------------------
# KPI METRICS
# ------------------------------------

completed = len(
    df[df["Status"] == "Completed"]
)

missed = len(
    df[df["Status"] == "Missed"]
)

completion_rate = (
    completed /
    (completed + missed)
) * 100

profit = (
    df[df["Status"] == "Completed"]
    ["Profit"]
    .sum()
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "✅ Completed",
        completed
    )

with col2:
    st.metric(
        "❌ Missed",
        missed
    )

with col3:
    st.metric(
        "📈 Completion %",
        f"{completion_rate:.1f}%"
    )

with col4:
    st.metric(
        "💰 Profit",
        profit
    )

# ------------------------------------
# CHARTS ROW 1
# ------------------------------------

left, right = st.columns(2)

with left:

    pie = px.pie(
        names=[
            "Completed",
            "Missed"
        ],
        values=[
            completed,
            missed
        ],
        title="Task Completion Status"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

with right:

    profit_chart = px.bar(
        df,
        x="Task",
        y="Profit",
        color="Status",
        title="Profit Per Task"
    )

    st.plotly_chart(
        profit_chart,
        use_container_width=True
    )

# ------------------------------------
# CHARTS ROW 2
# ------------------------------------

left, right = st.columns(2)

with left:

    priority_chart = px.histogram(
        df,
        x="Priority",
        color="Status",
        title="Priority Distribution"
    )

    st.plotly_chart(
        priority_chart,
        use_container_width=True
    )

with right:

    st.subheader(
        "Dependency Graph"
    )

    G = nx.DiGraph()

    G.add_edge(
        "Database Setup",
        "Backend API"
    )

    G.add_edge(
        "Backend API",
        "Frontend UI"
    )

    G.add_edge(
        "Frontend UI",
        "Testing"
    )

    G.add_edge(
        "Testing",
        "Deployment"
    )

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    nx.draw(
        G,
        with_labels=True,
        node_size=3000,
        font_size=10,
        ax=ax
    )

    st.pyplot(fig)

# ------------------------------------
# GANTT CHART
# ------------------------------------

st.subheader(
    "📅 Gantt Chart"
)

st.image(
    "outputs/gantt_chart.png",
    use_container_width=True
)

# ------------------------------------
# DOWNLOADS
# ------------------------------------

st.subheader(
    "📥 Download Reports"
)

with open(
    "outputs/schedule_report.csv",
    "rb"
) as file:

    st.download_button(
        label="Download CSV Report",
        data=file,
        file_name="schedule_report.csv",
        mime="text/csv"
    )

with open(
    "outputs/schedule_report.txt",
    "rb"
) as file:

    st.download_button(
        label="Download TXT Report",
        data=file,
        file_name="schedule_report.txt",
        mime="text/plain"
    )