@echo off

REM **Required:** Adjust the paths below to match your setup
SET python_script="C:\Users\miguel top\Desktop\lexer\Connector.py" 

REM **Check if a filename is provided**
IF "%~1"=="" (
    ECHO Error: Please provide a filename.
    ECHO Usage: %0 filename.txt
    EXIT /B 1
)

REM **Call the Python script and pass the filename**
python %python_script% %~1

REM **Optional: Indicate completion**
ECHO Code Compiled!
