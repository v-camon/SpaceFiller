# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all

block_cipher = None

# --- RECOLECCIÓN AUTOMÁTICA DE LIBRERÍAS REBELDES ---
# 1. Packaging (la que arreglamos antes)
datas_pkg, binaries_pkg, hiddenimports_pkg = collect_all('packaging')
# 2. Darkdetect (la nueva rebelde)
datas_dd, binaries_dd, hiddenimports_dd = collect_all('darkdetect')
# ----------------------------------------------------

a = Analysis(
    ['SpaceFiller.py'],
    pathex=[],
    # SUMAMOS LOS BINARIOS DE AMBAS LIBRERÍAS
    binaries=binaries_pkg + binaries_dd,
    
    # SUMAMOS LOS DATOS DE CUSTOMTKINTER + PACKAGING + DARKDETECT
    datas=[('logo.ico', '.'), ('C:\\Users\\Manchas73\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python313\\site-packages\\customtkinter', 'customtkinter')] + datas_pkg + datas_dd,
    
    # SUMAMOS LOS IMPORTS MANUALES + PACKAGING + DARKDETECT
    # (Nota: he quitado 'darkdetect' de la lista manual porque ya va en hiddenimports_dd)
    hiddenimports=['platform', 'tkinter.font', 'tkinter.ttk'] + hiddenimports_pkg + hiddenimports_dd,
    
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='SpaceFiller',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['logo.ico'],
)