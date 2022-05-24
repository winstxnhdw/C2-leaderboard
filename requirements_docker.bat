@echo off
set powershell_command=Start-Process '.\Docker Desktop Installer.exe' -Wait 'install --accept-license'
PowerShell -NoProfile -ExecutionPolicy Bypass -Command %powershell_command%