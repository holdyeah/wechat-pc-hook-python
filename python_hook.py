
#-*- coding: utf-8 -*-
import win32api,win32process,win32con,ctypes,psutil
from ctypes import * 

PAGE_READWRITE = 0x00000040
PROCESS_ALL_ACCESS =  (0x000F0000|0x00100000|0xFFF)
VIRTUAL_MEM = (0x00001000 | 0x00002000)
dll_path = b"C:\\SendMessage.dll"
print(dll_path)
dll_len = len(dll_path)
kernel32 = ctypes.windll.kernel32
#第一步获取整个系统的进程快照 第二步在快照中去比对进程名
for proc in psutil.process_iter():
    try:
        if proc.name() == 'WeChat.exe':
            print(proc)
            break
        else:
            proc = 0
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        print ("无 Permission or process")
#第三步用找到的pid去打开进程获取到句柄

if proc == 0:
    print("没有找到微信或者微信没有启动")
else:
    h_process=kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,(proc.pid))
    print('%x'%h_process)
    if not h_process:
        print('进程打开失败权限不足')
    else:
        arg_adress=kernel32.VirtualAllocEx(h_process,None,dll_len*10,VIRTUAL_MEM,PAGE_READWRITE)
        print('%x'%arg_adress)
        NULL = c_int(0)
        whhh=kernel32.WriteProcessMemory(h_process,arg_adress,dll_path,dll_len*10,NULL)
        h_kernel32 = win32api.GetModuleHandle("kernel32.dll")
        h_loadlib = win32api.GetProcAddress(h_kernel32, 'LoadLibraryA')
        print('%x'%h_kernel32,'%x'%h_loadlib)
        thread_id = c_ulong(0)
        c_remt = kernel32.CreateRemoteThread(h_process,None,0,h_loadlib,arg_adress,0,byref(thread_id))
        print('%x'%c_remt)
        if not c_remt:
            print("[!] Failed to inject DLL, exit...")
