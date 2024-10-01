# -*- mode: python ; coding: utf-8 -*-

icon_path = 'icon.ico'
icon_png = 'icon.png'
block_cipher = None

a = Analysis(
    ['PS5PayloadInjector.py'],
    pathex=[],
    binaries=[],
    datas=[(icon_path, '.'),(icon_png,'.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    upx_dir='C:\\UPX',
    upx=True,
    cipher=block_cipher,
    noarchive=False
)
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher,
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PS5 Payload Injector',
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
    icon=['icon.ico'],
)
