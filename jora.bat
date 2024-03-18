REM **Required:** Adjust the paths below to match your setup
SET python_script="C:\Users\miguel top\Desktop\lexer\Connector.py" 

REM **Check if a filename is provided**
ECHO %~1
IF "%~1"=="" (
    ECHO Error: Please provide a filename.
    ECHO Usage: %0 filename.name
  EXIT /B 1
)

REM **Extract the base filename without extension**
SET base_filename=%~n1

REM **Construct the new filename with .py extension**
SET new_filename=%base_filename%.py

REM **Call the Python script and pass the new filename**
python %python_script% %~1
@REM python %python_script% %new_filename%

REM **Optional: Indicate completion**
ECHO Code Compiled!
