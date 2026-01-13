"""
Project configuration for Credit Risk Baseline.

Keep all reusable constants here so notebooks are reproducible and consistent.
"""

# --- Target definition ---
BAD_STATUSES = [
    "Charged Off",
    "Default",
    "Late (31-120 days)",
    "Late (16-30 days)",
]

GOOD_STATUSES = [
    "Fully Paid",
]

TARGET_COL = "target_default"


# --- Dates / time split ---
ISSUE_DATE_COL = "issue_d"
ISSUE_DATE_FORMAT = "%b-%Y"   # Lending Club style: 'Dec-2016'


# --- Leakage / post-origination columns ---
LEAKAGE_COLS = [
    "last_pymnt_d",
    "last_pymnt_amnt",
    "total_pymnt",
    "total_pymnt_inv",
    "total_rec_prncp",
    "total_rec_int",
    "total_rec_late_fee",
    "recoveries",
    "collection_recovery_fee",
    "next_pymnt_d",
    "last_credit_pull_d",  # sometimes borderline; exclude for strict origination-only
]


# --- Feature handling defaults ---
DTI_COL = "dti"
DTI_CAP = 60.0

# Common numeric caps (optional; can expand later)
REV_UTIL_COL = "revol_util"
REV_UTIL_CAP = 100.0

# Columns often safe for origination-time modeling (starter allowlist concept)
# (We'll refine in feature_prep.)
CANDIDATE_FEATURES_HINT = [
    "loan_amnt", "term", "int_rate", "installment",
    "grade", "sub_grade", "emp_length", "home_ownership",
    "annual_inc", "verification_status", "purpose",
    "addr_state", "dti", "delinq_2yrs", "inq_last_6mths",
    "open_acc", "pub_rec", "revol_bal", "revol_util",
    "total_acc", "application_type",
]


# --- Paths (relative to repo root) ---
# --- Paths (Colab + Google Drive friendly) ---
# Set these in the notebook after mounting drive, if you want.
DEFAULT_DRIVE_ROOT = "/content/drive/MyDrive"

# Change these once you decide where the file lives in Drive:
RAW_DATA_PATH = "/content/drive/MyDrive/Credit Risk Baseline Data/loan.csv"

# Where to write processed artifacts (optional)
PROCESSED_DATA_DIR = "/content/drive/MyDrive/Credit Risk Baseline Data/processed"
TRAIN_PATH = f"{PROCESSED_DATA_DIR}/train.parquet"
VAL_PATH   = f"{PROCESSED_DATA_DIR}/val.parquet"

