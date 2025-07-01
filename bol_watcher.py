import time
from pathlib import Path

INCOMING_DIR = Path("Incoming")

def get_unprocessed_pdfs():
    return [f for f in INCOMING_DIR.glob("*.pdf") if not f.name.startswith("parsed_")]

def mark_as_parsed(file_path):
    new_name = file_path.with_name(f"parsed_{file_path.name}")
    file_path.rename(new_name)

def watch_for_bol_files(process_function):
    while True:
        files = get_unprocessed_pdfs()
        for file in files:
            print(f"Processing: {file.name}")
            process_function(file)
            mark_as_parsed(file)
        time.sleep(5)  # Check every 5 seconds

from report_tools import log_review_entry
from bol_parser import parse_bol_pdf

def process_pdf(file_path):
    shipment = parse_bol_pdf(file_path)
    missing_fields = [k for k, v in shipment.items() if v in ("", "—")]

    log_review_entry(
        data=shipment,
        status="Flagged" if missing_fields else "Accepted",
        missing_fields=missing_fields
    )

if __name__ == "__main__":
    watch_for_bol_files(process_pdf)

