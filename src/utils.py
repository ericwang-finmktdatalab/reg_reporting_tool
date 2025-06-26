# Helper functions


# Schema Validation (column level) - Ensure data has required columns before processing.
def validate_schema(df, required_cols) -> int:
    unmatched_col = [col for col in required_cols if col not in df.columns]
    if unmatched_col:
        print(f"[ERROR] Columns do not match schema: {unmatched_col}")
        return 1
    else:
        return 0


# Event Logging - print/log wrapper for consistent status updates.
def log_event(msg: str):
    print(f"[INFO] {msg}")


# XML Utility
def dict_to_xml(tag, d):
    from xml.etree.ElementTree import Element, SubElement
    elem = Element(tag)
    for key, val in d.items():
        child = SubElement(elem, key)
        child.text = str(val)
    return elem


# Date Parsing - Convert string dates.
from datetime import datetime

def parse_date(date_str, fmt="%Y-%m-%d"):
    try:
        return datetime.strptime(date_str, fmt).date()
    except ValueError:
        return None


# UUID Generator - Generates trade or transaction identifiers.
import uuid

def generate_uuid():
    return str(uuid.uuid4())
