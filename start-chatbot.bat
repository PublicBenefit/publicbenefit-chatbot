@echo off

REM Check if Flask server (python.exe) is already running
tasklist | findstr /I "python.exe" >nul
if %errorlevel%==0 (
    echo ChatBot is already running.
    pause
    exit
)

:loop
echo Starting PublicBenefit ChatBot...
start /MIN cmd /c python publicbenefit-chatbot.py

timeout /t 5 /nobreak >nul
start http://192.168.1.214:5000/

:wait
timeout /t 60 >nul
tasklist | findstr /I "python.exe" >nul
if errorlevel 1 (
    echo Flask server stopped. Restarting...
    goto loop
) else (
    goto wait
)
