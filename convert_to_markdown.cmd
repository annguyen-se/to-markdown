@echo off
setlocal

if "%~1"=="" (
    exit /b 1
)

set "INPUT=%~1"
set "OUTPUT=%~dpn1.md"
set "LOG=%~dpn1.to-markdown.log"
set "PROJECT_DIR=%~dp0"
set "PYTHON=%PROJECT_DIR%.venv\Scripts\python.exe"

(
    echo === to-markdown conversion started ===
    echo Date: %DATE% %TIME%
    echo Input: %INPUT%
    echo Output: %OUTPUT%
    echo Project: %PROJECT_DIR%
    echo Python: %PYTHON%
    echo.
) > "%LOG%"

if not exist "%PYTHON%" (
    echo Python virtual environment was not found: %PYTHON% >> "%LOG%"
    exit /b 1
)

"%PYTHON%" -m to_markdown "%INPUT%" -o "%OUTPUT%" >> "%LOG%" 2>&1

if errorlevel 1 (
    echo. >> "%LOG%"
    echo Failed to convert: %INPUT% >> "%LOG%"
    exit /b 1
)

if not exist "%OUTPUT%" (
    echo. >> "%LOG%"
    echo Conversion finished but output file was not created. >> "%LOG%"
    exit /b 1
)

echo Created: %OUTPUT% >> "%LOG%"
endlocal
