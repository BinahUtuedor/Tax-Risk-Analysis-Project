"""
Configuration Module (ROBUST VERSION)
====================================

Fixes:
- file/folder conflicts (Windows + OneDrive issues)
- safe directory recovery
- run-based outputs
"""

from pathlib import Path
from datetime import datetime

# --------------------------------------------------
# PROJECT ROOT
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent


# --------------------------------------------------
# DATA FOLDERS
# --------------------------------------------------

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"


# --------------------------------------------------
# OUTPUT FOLDERS
# --------------------------------------------------

OUTPUT_DIR = BASE_DIR / "outputs"


# --------------------------------------------------
# RUN SYSTEM
# --------------------------------------------------

RUN_ID = datetime.now().strftime("run_%Y-%m-%d_%H-%M-%S")
RUN_DIR = OUTPUT_DIR / RUN_ID

CHART_DIR = RUN_DIR / "charts"
REPORT_DIR = RUN_DIR / "reports"
MODEL_DIR = RUN_DIR / "models"


# --------------------------------------------------
# SAFE DIRECTORY CREATION (FIXED)
# --------------------------------------------------

def _safe_mkdir(path: Path):
    """
    Creates directory safely.
    If a FILE exists with same name → raises clear error.
    """

    if path.exists():

        if path.is_file():
            raise RuntimeError(
                f"""
❌ CONFIG ERROR: Path exists as a FILE, not a folder:

{path}

Fix:
1. Delete this file
2. Create a folder with the same name
                """
            )

        return  # already valid folder

    path.mkdir(parents=True, exist_ok=True)


def _init_dirs():
    """
    Initialize full project structure safely.
    """

    folders = [
        DATA_DIR,
        RAW_DATA_DIR,
        PROCESSED_DATA_DIR,
        OUTPUT_DIR,
        RUN_DIR,
        CHART_DIR,
        REPORT_DIR,
        MODEL_DIR
    ]

    for folder in folders:
        _safe_mkdir(folder)


# initialize on import
_init_dirs()


# --------------------------------------------------
# GLOBAL SETTINGS
# --------------------------------------------------

SEED = 42
N_TAXPAYERS = 2000