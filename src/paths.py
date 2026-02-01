from pathlib import Path

# Project root: STAT587_DS1_HW2/
ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "reports" / "figures"
TAB_DIR = ROOT / "reports" / "tables"


def ensure_dirs() -> None:
    """Create figure/table directories if they do not exist."""
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    TAB_DIR.mkdir(parents=True, exist_ok=True)