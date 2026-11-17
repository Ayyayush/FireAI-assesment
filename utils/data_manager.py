from pathlib import Path
import pandas as pd

# --------------------------------------------------
# PROJECT PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

JOBS_FILE = DATA_DIR / "data.csv"
STOCK_FILE = DATA_DIR / "stock.csv"


# --------------------------------------------------
# CSV SCHEMAS
# --------------------------------------------------

JOB_COLUMNS = [
    "job_id",
    "received_time",
    "source_channel",
    "customer_label",
    "document_label",
    "pages",
    "copies",
    "print_type",
    "requested_sequence",
    "status",
    "rate_per_page",
]

STOCK_COLUMNS = ["product_id", "product_name", "current_quantity", "minimum_quantity"]


# --------------------------------------------------
# DIRECTORY AND FILE INITIALIZATION
# --------------------------------------------------


def initialize_data_files():
    """
    Create the data directory and CSV files
    with headers if they do not already exist.
    """

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    for file_path, columns in [(JOBS_FILE, JOB_COLUMNS), (STOCK_FILE, STOCK_COLUMNS)]:
        if not file_path.exists():
            pd.DataFrame(columns=columns).to_csv(file_path, index=False)


# --------------------------------------------------
# GENERIC CSV LOADER
# --------------------------------------------------


def load_csv(file_path, expected_columns):
    """
    Load a CSV file and validate its columns.

    Returns:
        pandas DataFrame
    """

    if not file_path.exists():
        raise FileNotFoundError(f"Required file not found: {file_path}")

    try:
        df = pd.read_csv(file_path)

    except pd.errors.EmptyDataError as error:
        raise ValueError(f"{file_path.name} is empty or has no header.") from error

    except pd.errors.ParserError as error:
        raise ValueError(
            f"Could not parse {file_path.name}. " "Check its CSV formatting."
        ) from error

    missing_columns = [
        column for column in expected_columns if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Invalid {file_path.name}. " f"Missing columns: {missing_columns}"
        )

    return df[expected_columns]


# --------------------------------------------------
# JOB DATA FUNCTIONS
# --------------------------------------------------


def load_jobs():
    """Load all printing and photocopying jobs."""

    return load_csv(JOBS_FILE, JOB_COLUMNS)


def save_jobs(df):
    """Save the job records to data.csv."""

    if not set(JOB_COLUMNS).issubset(df.columns):
        raise ValueError("Job DataFrame has an invalid schema.")

    df[JOB_COLUMNS].to_csv(JOBS_FILE, index=False)


# --------------------------------------------------
# STOCK DATA FUNCTIONS
# --------------------------------------------------


def load_stock():
    """Load all stationery stock records."""

    return load_csv(STOCK_FILE, STOCK_COLUMNS)


def save_stock(df):
    """Save stationery records to stock.csv."""

    if not set(STOCK_COLUMNS).issubset(df.columns):
        raise ValueError("Stock DataFrame has an invalid schema.")

    df[STOCK_COLUMNS].to_csv(STOCK_FILE, index=False)
