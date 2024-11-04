Ansible так же установлен на [192.168.1.201](https://internal.rtp.by:8445/articles/SER-A-6324304/1921681201-dockerskbrtp)

## Для разворачивания нового сервера Ansible необходимо:

1.  Склонить текущий репозиторий git@internal.rtp.by:common/ansible.git

2.  Установить Ansible:

```
sudo apt-add-repository ppa:ansible/ansible

sudo apt-get update

sudo apt-get install ansible 
```

3.  Перейти в директорию с файлами hosts.txt(хостами) cputempinstall.yml(конфигурацией Ansible) относительно задачи

4.  Выполнить Команды для запуска и применения конфигурации Ansible:

**ansible-playbook -i hosts.txt cputempinstall.yml -k**

или

**ansible-playbook -i hosts.txt cputempinstall.yml** - флаг -k запрашивает пароль пользователя под которым выполняется конфигурация Ансибл, если этого флага нет - надо прописать ansible_password=... в файле hosts.txt в явном виде.



## На хостах к которым будет применяться конфигурация Ansible должно быть установленно **_installsshserver.ps1_** или прописанны команды под администратором в powershell:

```
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

Start-Service sshd

Set-Service -Name sshd -StartupType 'Automatic'

if (!(Get-NetFirewallRule -Name "OpenSSH-Server-In-TCP" -ErrorAction SilentlyContinue | Select-Object Name, Enabled)) {
    Write-Output "Firewall Rule 'OpenSSH-Server-In-TCP' does not exist, creating it..."
    New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
} else {
    Write-Output "Firewall rule 'OpenSSH-Server-In-TCP' has been created and exists."
}

Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'
```
