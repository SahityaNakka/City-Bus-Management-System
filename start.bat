@echo off
title CityTransit Bus Management System
echo ====================================================
echo Starting CityTransit Bus Management System (DEMO)...
echo ====================================================
cd /d "%~dp0backend"
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" run.py
) else (
    python run.py
)
pause
