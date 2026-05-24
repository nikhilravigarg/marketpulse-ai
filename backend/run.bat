@echo off
setlocal enabledelayedexpansion

REM Navigate to backend folder
cd /d %~dp0

if not exist venv\Scripts\activate.bat (
    echo Virtual environment not found. Run build.bat first:
    echo    build.bat
    exit /b 1
)

call venv\Scripts\activate.bat
if errorlevel 1 (
    echo Failed to activate virtual environment.
    exit /b 1
)

echo Starting FastAPI server...
uvicorn app.main:app --reload
exit /b %ERRORLEVEL%

