import streamlit as st
import csv
import io
import threading
from report_tools import review_log
from bol_watcher import watch_for_bol_files, process_pdf
from autogen_main import launch_agent_backend

st.set_page_config(page_title="Loading Dock", layout="centered")
st.title("📦 Loading Dock Control Panel")

# Track state
if "system_online" not in st.session_state:
    st.session_state.system_online = False

def start_backend():
    # Start the watcher and AutoGen backend in background threads
    threading.Thread(target=watch_for_bol_files, args=(process_pdf,), daemon=True).start()
    launch_agent_backend()
    st.session_state.system_online = True

# Startup control
if not st.session_state.system_online:
    if st.button("🟢 Power On"):
        start_backend()
        st.success("System started: Agents + Watcher Online")
else:
    st.success("✅ System is Running")

# Generate and download manifest
def generate_csv_from_log(log):
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=[
        "Order ID", "Status", "Type", "Destination", "Missing Fields", "Timestamp"
    ])
    writer.writeheader()
    writer.writerows(log)
    return output.getvalue()

if st.button("📤 Generate Manifest Report"):
    if not review_log:
        st.warning("No shipments have been processed yet.")
    else:
        csv_data = generate_csv_from_log(review_log)
        st.download_button(
            label="Download Manifest as CSV",
            data=csv_data,
            file_name="shipment_manifest.csv",
            mime="text/csv"
        )
