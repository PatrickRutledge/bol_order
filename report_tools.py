# Global log storage
review_log = []



# Logging function to record reviewed shipment data
def log_review_entry(data: dict, status: str, missing_fields: list):
    from datetime import datetime
    review_log.append({
        "Order ID": data.get("shipment_id", "—"),
        "Status": status,
        "Type": data.get("shipment_type", "Unknown"),
        "Destination": data.get("destination", "—"),
        "Missing Fields": ", ".join(missing_fields) if missing_fields else "—",
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


def generate_report() -> str:
    if not review_log:
        return "No shipments have been processed yet."
    
    header = "| Order ID | Status | Type | Destination | Missing Fields | Timestamp |\n"
    divider = "|----------|--------|------|-------------|----------------|---------------------|\n"
    rows = [
        f"| {entry['Order ID']} | {entry['Status']} | {entry['Type']} | {entry['Destination']} | {entry['Missing Fields']} | {entry['Timestamp']} |"
        for entry in review_log
    ]
    return header + divider + "\n".join(rows)
