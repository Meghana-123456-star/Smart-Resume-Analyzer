@echo off
REM Smart Resume Analyzer - Windows Startup Script

echo.
echo =====================================
echo Smart Resume Analyzer
echo =====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

echo ✓ Python found

REM Create uploads folder if not exists
if not exist uploads mkdir uploads

REM Install dependencies if requirements.txt exists
if exist requirements.txt (
    echo Installing dependencies...
    pip install -q -r requirements.txt
    echo ✓ Dependencies installed
) else (
    echo WARNING: requirements.txt not found
)

echo.
echo ✓ Starting Smart Resume Analyzer...
echo.
echo 🌐 Open your browser and go to: http://localhost:5000
echo.
echo Press CTRL+C to stop the server
echo.

python app.py

pause
