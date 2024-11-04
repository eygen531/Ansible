@echo off
mkdir C:\skb
echo Foldelr C:\skb successfully created.

:: Unzip arhive cputemp.zip from current directory to folder
powershell -command "Expand-Archive -Path '%CD%\cputemp.zip' -DestinationPath 'C:\skb'"
echo Arhive cputemp.zip successfully unzip in C:\skb.

:: Install  windows_exporter-0.25.1-amd64.msi
msiexec /i "C:\skb\windows_exporter-0.25.1-amd64.msi"
echo windows_exporter installation complete.

:: Execution PowerShell addstartupcpu_py.ps1 run with administrator rights
powershell -command "Start-Process powershell -ArgumentList '-ExecutionPolicy Bypass -File \"C:\skb\addstartupcpu_py.ps1\"' -Verb RunAs"
echo addstartupcpu_py.ps1 run with administrator rights.

pause