@echo off
set powershell_command=Start-Process '.\bin\Docker Desktop Installer.exe' -Wait 'install --accept-license --backend=wsl-2'
PowerShell -NoProfile -ExecutionPolicy Bypass -Command %powershell_command%
