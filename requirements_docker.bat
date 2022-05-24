@echo off
set powershell_command=Start-Process '.\bin\Docker Desktop Installer.exe' -Wait 'install --accept-license'
PowerShell -NoProfile -ExecutionPolicy Bypass -Command %powershell_command%