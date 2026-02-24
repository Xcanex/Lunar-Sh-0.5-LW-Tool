@echo off
title Lunar - Setup
echo =======================================================
echo              LUNAR TOOL KIT SETUP (WINDOWS)
echo =======================================================
echo.
echo Installing Python dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.
echo =======================================================
echo Setup Complete! You can now run start.bat
echo =======================================================
pause
