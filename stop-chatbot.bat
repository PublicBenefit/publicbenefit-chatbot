@echo off
echo Stopping PublicBenefit ChatBot...

REM Find and kill Python processes (Flask)
taskkill /f /im python.exe

echo ChatBot server stopped successfully.
pause
