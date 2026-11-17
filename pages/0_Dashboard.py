import streamlit as st
import pandas as pd

from utils.job_manager import get_all_jobs
from utils.inventory_manager import get_all_stock, get_low_stock_items

# ==================================================
# 1. CUSTOM CSS
# ==================================================

st.markdown(
    """
<style>
    .main {
        background-color: #f8fafc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.04);
    }

    div[data-testid="stMetric"] label {
        color: #475569 !important;
    }

    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #0f172a !important;
        font-weight: 700;
    }

    div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
        color: #475569 !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    h1, h2, h3 {
        color: #0f172a;
    }
</style>
""",
    unsafe_allow_html=True,
)


# ==================================================
# 2. LOAD DATA
# ==================================================

jobs = get_all_jobs()
stock = get_all_stock()
low_stock = get_low_stock_items()


# ==================================================
# 3. SIDEBAR DETAILS
# ==================================================

with st.sidebar:

    st.title("🖨️ PrintDesk")

    st.caption("Print Shop Management System")

    st.divider()

    st.markdown("**Shop Details**")
    st.write("Print Mega Mess")
    st.write("NIT Jamshedpur")

    st.divider()

    st.caption("PrintDesk v1.0")


# ==================================================
# 4. DASHBOARD HEADER
# ==================================================

st.title("🖨️ Print Shop Dashboard")

st.write(
    "Manage printing requests, track job progress " "and monitor stationery stock."
)

st.divider()


# ==================================================
# 5. JOB STATISTICS
# ==================================================

total_jobs = len(jobs)

pending_jobs = 0
processing_jobs = 0
completed_jobs = 0

if not jobs.empty:

    pending_jobs = (jobs["status"] == "Pending").sum()

    processing_jobs = (jobs["status"] == "Processing").sum()

    completed_jobs = (jobs["status"] == "Completed").sum()


# ==================================================
# 6. DISPLAY JOB METRICS
# ==================================================

st.subheader("Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Jobs", total_jobs)

col2.metric("Pending Jobs", pending_jobs)

col3.metric("Processing Jobs", processing_jobs)

col4.metric("Completed Jobs", completed_jobs)


# ==================================================
# 7. INVENTORY METRICS
# ==================================================

st.write("")

col1, col2 = st.columns(2)

col1.metric("Stationery Products", len(stock))

col2.metric("Low Stock Alerts", len(low_stock))


# ==================================================
# 8. RECENT PRINTING JOBS
# ==================================================

st.divider()

st.subheader("📋 Recent Printing Jobs")

if jobs.empty:

    st.info(
        "No printing jobs have been registered yet. "
        "Add jobs through the Job Register."
    )

else:

    recent_jobs = jobs.copy()

    recent_jobs["received_time"] = pd.to_datetime(
        recent_jobs["received_time"], errors="coerce"
    )

    recent_jobs = recent_jobs.sort_values(
        by="received_time", ascending=False, na_position="last"
    )

    display_columns = [
        "job_id",
        "received_time",
        "source_channel",
        "document_label",
        "pages",
        "copies",
        "print_type",
        "status",
    ]

    st.dataframe(
        recent_jobs[display_columns].head(10), use_container_width=True, hide_index=True
    )


# ==================================================
# 9. STATIONERY STOCK ALERTS
# ==================================================

st.divider()

st.subheader("📦 Stationery Stock Alerts")

if stock.empty:

    st.info(
        "No stationery products have been added yet. "
        "Add products through the Inventory section."
    )

elif low_stock.empty:

    st.success(
        "All recorded stationery products are " "above their minimum stock levels."
    )

else:

    st.warning(f"{len(low_stock)} product(s) require stock attention.")

    st.dataframe(low_stock, use_container_width=True, hide_index=True)


# ==================================================
# 10. FOOTER
# ==================================================

st.divider()

st.caption("PrintDesk | A lightweight print shop management tool")

st.caption("Built using Python, Streamlit, Pandas and CSV.")
