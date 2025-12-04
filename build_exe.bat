@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo Building Executable...
pyinstaller --noconfirm --onefile --windowed --collect-all customtkinter --name "JuegoDelImpostor" impostor_gui.py

echo.
echo Build complete! Check the 'dist' folder for your .exe file.
pause
