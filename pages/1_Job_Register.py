import streamlit as st
import pandas as pd

from utils.job_manager import add_job, get_all_jobs, search_jobs, update_job_status

from utils.billing import get_rate

# ==================================================
# 1. PAGE HEADER
# ==================================================

st.title("📋 Job Register")

st.write(
    "Register incoming printing requests, search existing "
    "jobs and manage their progress."
)

st.divider()


# ==================================================
# 2. JOB STATISTICS
# ==================================================

jobs = get_all_jobs()

total_jobs = len(jobs)

if jobs.empty:
    pending_jobs = 0
    processing_jobs = 0
    completed_jobs = 0

else:
    statuses = jobs["status"].fillna("").astype(str).str.strip()

    pending_jobs = (statuses == "Pending").sum()
    processing_jobs = (statuses == "Processing").sum()
    completed_jobs = (statuses == "Completed").sum()


col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Jobs", total_jobs)
col2.metric("Pending", pending_jobs)
col3.metric("Processing", processing_jobs)
col4.metric("Completed", completed_jobs)


# ==================================================
# 3. REGISTER NEW JOB
# ==================================================

st.divider()

st.subheader("➕ Register New Printing Job")

with st.form("job_registration_form", clear_on_submit=True):

    col1, col2 = st.columns(2)

    with col1:

        source_channel = st.selectbox(
            "Received Through", ["WhatsApp", "Email", "Physical"]
        )

        customer_label = st.text_input(
            "Customer Reference", placeholder="Example: Customer 01"
        )

        document_label = st.text_input(
            "Document Name", placeholder="Example: Lab Assignment"
        )

        print_type = st.selectbox("Printing Type", ["Printout", "Photocopy"])

    with col2:

        pages = st.number_input(
            "Number of Pages", min_value=1, max_value=10000, value=1, step=1
        )

        copies = st.number_input(
            "Number of Copies", min_value=1, max_value=1000, value=1, step=1
        )

        requested_sequence = st.number_input(
            "Requested Sequence", min_value=1, max_value=10000, value=1, step=1
        )

    # Calculate estimated cost
    rate = get_rate(print_type)

    estimated_cost = int(pages) * int(copies) * rate

    st.info(f"Rate: ₹{rate}/page | " f"Estimated Cost: ₹{estimated_cost}")

    submitted = st.form_submit_button("Register Job", use_container_width=True)

    if submitted:

        try:

            job = add_job(
                source_channel=source_channel,
                customer_label=customer_label,
                document_label=document_label,
                pages=int(pages),
                copies=int(copies),
                print_type=print_type,
                requested_sequence=int(requested_sequence),
            )

            st.success(f"Job registered successfully! " f"Job ID: {job['job_id']}")

            st.rerun()

        except ValueError as error:

            st.error(str(error))


# ==================================================
# 4. SEARCH EXISTING JOBS
# ==================================================

st.divider()

st.subheader("🔍 Search Printing Jobs")

search_term = st.text_input(
    "Search by Job ID, Customer or Document",
    placeholder="Example: JOB001 or Lab Assignment",
)

if search_term.strip():

    displayed_jobs = search_jobs(search_term)

else:

    displayed_jobs = get_all_jobs()


# ==================================================
# 5. DISPLAY JOB REGISTER
# ==================================================

st.subheader("All Printing Jobs")

if displayed_jobs.empty:

    st.info("No matching printing jobs found.")

else:

    display_jobs = displayed_jobs.copy()

    display_jobs["received_time"] = pd.to_datetime(
        display_jobs["received_time"], errors="coerce"
    )

    display_jobs["status"] = (
        display_jobs["status"].fillna("Not assigned").replace("", "Not assigned")
    )

    display_columns = [
        "job_id",
        "received_time",
        "source_channel",
        "customer_label",
        "document_label",
        "pages",
        "copies",
        "print_type",
        "requested_sequence",
        "rate_per_page",
        "status",
    ]

    st.dataframe(
        display_jobs[display_columns], use_container_width=True, hide_index=True
    )

    st.caption(f"Showing {len(displayed_jobs)} job(s).")


# ==================================================
# 6. UPDATE JOB STATUS
# ==================================================

st.divider()

st.subheader("🔄 Update Job Status")

all_jobs = get_all_jobs()

if all_jobs.empty:

    st.info("Register a job before updating its status.")

else:

    job_ids = all_jobs["job_id"].astype(str).tolist()

    selected_job = st.selectbox("Select Job ID", job_ids)

    selected_record = all_jobs.loc[all_jobs["job_id"].astype(str) == selected_job].iloc[
        0
    ]

    current_status = selected_record["status"]

    valid_statuses = ["Pending", "Processing", "Completed"]

    # Handle missing or invalid status values
    if pd.isna(current_status):
        current_status = None

    elif current_status not in valid_statuses:
        current_status = None

    if current_status is None:

        st.info("Current Status: Not assigned")

        default_index = 0

    else:

        st.write(f"Current Status: **{current_status}**")

        default_index = valid_statuses.index(current_status)

    new_status = st.selectbox("Select New Status", valid_statuses, index=default_index)

    if st.button("Update Status", use_container_width=True):

        try:

            update_job_status(job_id=selected_job, new_status=new_status)

            st.success(f"{selected_job} updated to {new_status}.")

            st.rerun()

        except ValueError as error:

            st.error(str(error))


# ==================================================
# 7. FOOTER
# ==================================================

st.divider()

st.caption("PrintDesk | Job Registration and Tracking")
