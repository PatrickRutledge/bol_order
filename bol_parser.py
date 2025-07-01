import pdfplumber

def extract_field(text, label):
    for line in text.splitlines():
        if label in line:
            return line.split(label)[-1].strip()
    return "—"

def parse_bol_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = "\n".join(
            page.extract_text() for page in pdf.pages if page.extract_text()
        )

    shipment = {
        "shipment_id": extract_field(text, "BOL #:"),
        "shipment_type": "Inbound",  # Default for now
        "destination": extract_field(text, "Ship To:"),
        "carrier": extract_field(text, "Carrier:"),
        "freight_class": extract_field(text, "Freight Class:")
    }

    return shipment
