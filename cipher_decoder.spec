# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['cipher_decoder.py'],
    pathex=[],
    binaries=[],
    datas=[('Classical Encryption App Icon.ico', '.'), ('Classical Encryption App Icon.png', '.'), ('Classical Encryption Suite Banner Gothic Font (1).png', '.'), ('Classical Encryption Suite Banner Gothic Font.png', '.'), ('Instagram_icon.png', '.'), ('LinkedIn_logo_initials.png', '.'), ('Mail_(iOS).png', '.'), ('words.txt', '.')],
    hiddenimports=[],
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
    name='cipher_decoder',
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
    icon=['Classical Encryption App Icon.ico'],
)
