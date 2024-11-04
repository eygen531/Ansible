$scriptPath = "C:\skb\cpu.bat"
$regPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"

if (-not (Test-Path $regPath)) {
     New-Item -Path $regPath -Force
}

New-ItemProperty -Path $regPath -Name "cputempppp" -Value $scriptPath -PropertyType String -Force
