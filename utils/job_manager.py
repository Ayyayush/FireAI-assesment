import pandas as pd
from datetime import datetime

from utils.data_manager import load_jobs, save_jobs
from utils.billing import get_rate

# --------------------------------------------------
# CONSTANTS
# --------------------------------------------------

VALID_CHANNELS = ["WhatsApp", "Email", "Physical"]
VALID_STATUSES = ["Pending", "Processing", "Completed"]


# --------------------------------------------------
# GENERATE UNIQUE JOB ID
# --------------------------------------------------


def generate_job_id():
    """
    Generate a unique sequential job ID.
    Example: JOB001, JOB002, JOB003
    """

    jobs = load_jobs()

    if jobs.empty:
        return "JOB001"

    numbers = []

    for job_id in jobs["job_id"].astype(str):
        if job_id.startswith("JOB") and job_id[3:].isdigit():
            numbers.append(int(job_id[3:]))

    next_number = max(numbers, default=0) + 1

    return f"JOB{next_number:03d}"


# --------------------------------------------------
# ADD NEW JOB
# --------------------------------------------------


def add_job(
    source_channel,
    customer_label,
    document_label,
    pages,
    copies,
    print_type,
    requested_sequence,
    status="Pending",
):
    """
    Validate and add a new printing job.
    """

    # Validate source channel
    if source_channel not in VALID_CHANNELS:
        raise ValueError("Invalid source channel.")

    # Validate job status
    if status not in VALID_STATUSES:
        raise ValueError("Invalid job status.")

    # Validate customer and document labels
    if not isinstance(customer_label, str) or not customer_label.strip():
        raise ValueError("Customer reference cannot be empty.")

    if not isinstance(document_label, str) or not document_label.strip():
        raise ValueError("Document label cannot be empty.")

    # Validate numeric fields
    if isinstance(pages, bool) or not isinstance(pages, int) or pages <= 0:
        raise ValueError("Pages must be a positive integer.")

    if isinstance(copies, bool) or not isinstance(copies, int) or copies <= 0:
        raise ValueError("Copies must be a positive integer.")

    if (
        isinstance(requested_sequence, bool)
        or not isinstance(requested_sequence, int)
        or requested_sequence <= 0
    ):
        raise ValueError("Requested sequence must be a positive integer.")

    # Get applicable printing rate
    rate = get_rate(print_type)

    # Load existing jobs
    jobs = load_jobs()

    # Create new job
    job = {
        "job_id": generate_job_id(),
        "received_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source_channel": source_channel,
        "customer_label": customer_label.strip(),
        "document_label": document_label.strip(),
        "pages": pages,
        "copies": copies,
        "print_type": print_type,
        "requested_sequence": requested_sequence,
        "status": status,
        "rate_per_page": rate,
    }

    # Append new job
    updated_jobs = pd.concat([jobs, pd.DataFrame([job])], ignore_index=True)

    save_jobs(updated_jobs)

    return job


# --------------------------------------------------
# GET ALL JOBS
# --------------------------------------------------


def get_all_jobs():
    """Return all printing and photocopying jobs."""

    return load_jobs()


# --------------------------------------------------
# SEARCH JOBS
# --------------------------------------------------


def search_jobs(search_term):
    """
    Search jobs by job ID, customer label,
    or document label.
    """

    jobs = load_jobs()

    if jobs.empty:
        return jobs

    search_term = str(search_term).strip().lower()

    if not search_term:
        return jobs

    mask = (
        jobs["job_id"].astype(str).str.lower().str.contains(search_term, na=False)
        | jobs["customer_label"]
        .astype(str)
        .str.lower()
        .str.contains(search_term, na=False)
        | jobs["document_label"]
        .astype(str)
        .str.lower()
        .str.contains(search_term, na=False)
    )

    return jobs[mask].reset_index(drop=True)


# --------------------------------------------------
# UPDATE JOB STATUS
# --------------------------------------------------


def update_job_status(job_id, new_status):
    """
    Update the status of an existing job.
    """

    if new_status not in VALID_STATUSES:
        raise ValueError("Invalid job status.")

    jobs = load_jobs()

    matching_jobs = jobs["job_id"] == job_id

    if not matching_jobs.any():
        raise ValueError(f"Job ID {job_id} not found.")

    jobs.loc[matching_jobs, "status"] = new_status

    save_jobs(jobs)

    return True
