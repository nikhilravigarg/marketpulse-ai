@echo off
setlocal enabledelayedexpansion

REM Navigate to backend folder
cd /d %~dp0

echo Creating or updating Python virtual environment...
if not exist venv\Scripts\activate.bat (
    python -m venv venv
    if errorlevel 1 (
        echo Failed to create virtual environment. Ensure Python is installed and on PATH.
        exit /b 1
    )
)

call venv\Scripts\activate.bat
if errorlevel 1 (
    echo Failed to activate virtual environment.
    exit /b 1
)

echo Installing dependencies from requirements.txt...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo Dependency installation failed.
    exit /b 1
)

echo.
echo Build complete. Run the backend with:
    run.bat
