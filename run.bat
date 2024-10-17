@echo off

if not exist "myenv\Scripts\activate" (
    echo Virtual environment not found. Creating a new one...
    python -m venv myenv
)

echo Activating the virtual environment...
call myenv\Scripts\activate

if exist requirements.txt (
    echo Installing dependencies...
    pip install -r requirements.txt
) else (
    echo requirements.txt not found. Make sure it exists.
    exit /b
)

echo Running the script...
python app.py

echo Script finished. Press any key to exit...
pause