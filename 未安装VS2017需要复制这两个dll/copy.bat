@echo off
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit

cd /d "%~dp0"

copy ucrtbased.dll C:\Windows\System32

copy ucrtbased.dll C:\Windows\SysWOW64

copy vcruntime140d.dll C:\Windows\System32

copy vcruntime140d.dll C:\Windows\SysWOW64

pause