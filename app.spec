# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files

streamlit_data = collect_data_files('streamlit')
streamlit_metadata = [('venv/Lib/site-packages/streamlit-1.46.1.dist-info', 'streamlit-1.46.1.dist-info')]

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=streamlit_data + streamlit_metadata,
    hiddenimports=[
        'streamlit',
        'streamlit.runtime',
        'streamlit.web',
        'streamlit.web.cli'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)


pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
