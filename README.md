README.md

# Loading Dock Control Panel

A local agent-based manifest processor built with Streamlit,
designed to detect incoming BOL files, generate CSV manifests,
and provide transparent controls for manual review and automation toggles.

# 🚀 Features
- Power On: Activates file watcher and agent orchestrator
- Generate Manifest Report: Produces structured CSV from BOL inputs
- Streamlit UI: Local dashboard served on http://localhost:8501
- Packaged `.exe` for single-click desktop deployment

# 🧱 Requirements
- Python 3.13+
- streamlit==1.46.1
- PyInstaller 6.14.1
- Windows 11 (tested)

# 🛠️ Local Dev
Run with live console:
streamlit run app.py

## To test before packaging:
- Confirm agents and watcher run as expected
- Drop a BOL file in /Incoming
- Ensure CSV is generated in /Generated/manifests

# 📦 Packaging into `.exe` (Streamlit Caveats)

## Problem:
Streamlit fails to launch after PyInstaller build due to:
# importlib.metadata.PackageNotFoundError: No package metadata was found for streamlit

## Solution:
Update `app.spec` to:
1. Add hidden imports
2. Manually include the .dist-info folder

# Minimal app.spec patch:

'''
from PyInstaller.utils.hooks import collect_data_files

streamlit_data = collect_data_files('streamlit')
streamlit_metadata = [('venv/Lib/site-packages/streamlit-1.46.1.dist-info', 'streamlit-1.46.1.dist-info')]

a = Analysis(
    ...
    datas=streamlit_data + streamlit_metadata,
    hiddenimports=[
        'streamlit',
        'streamlit.runtime',
        'streamlit.web',
        'streamlit.web.cli'
    ],
    ...
)
'''

# Then rebuild:
pyinstaller app.spec

# 🧪 Test Flow
1. Launch `app.exe` from `dist/`
2. Open http://localhost:8501
3. Click Power On
4. Drop a test BOL into /Incoming/
5. Generate manifest → verify CSV in /Generated/

# 🗂 Versioning
All updates to this README or the app’s behavior should be versioned using Git.
Major UX or packaging changes should bump the minor version (v0.x.0 → v0.(x+1).0).
Include short changelogs in commits.

# 📌 Notes
- Windows Defender may prompt firewall approval on first launch—this is normal
- Session state warnings from Streamlit during .exe runtime can be ignored
