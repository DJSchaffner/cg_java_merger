@echo off
pyinstaller --noconfirm --name "cg_java_merger" main.py --noconsole >nul 2>&1
@RD /S /Q "__pycache__"
@RD /S /Q "build" >nul 2>&1
if exist "build" rd /s /q "build"
DEL "cg_java_merger.spec"

echo Build complete