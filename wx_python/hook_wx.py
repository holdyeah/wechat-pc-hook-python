#-*- coding: utf-8 -*-
import os,ctypes,psutil,win32api
from ctypes import *
import shuju_data

def hook():
    PAGE_READWRITE = 0x00000040
    PROCESS_ALL_ACCESS =  (0x000F0000|0x00100000|0xFFF)
    VIRTUAL_MEM = (0x00001000 | 0x00002000)
    dll_path = bytes((os.path.abspath('.')+"\\SendMessage.dll").encode('utf-8'))
    print(dll_path)
    dll_len = len(dll_path)
    kernel32 = ctypes.windll.kernel32
    #第一步获取整个系统的进程快照
    pids = psutil.pids()
    #第二步在快照中去比对进程名
    for pid in pids:
        p= psutil.Process(pid)
        if p.name()=='WeChat.exe':
            shuju_data.wechet_lujian = p.cwd()
            break
        else:
            pid = 0
    #第三步用找到的pid去打开进程获取到句柄
    if pid == 0:
        return 0
    else:
        h_process=kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,(pid))
        if not h_process:
            return 0
        else:
            arg_adress=kernel32.VirtualAllocEx(h_process,None,dll_len*10,VIRTUAL_MEM,PAGE_READWRITE)
            NULL = c_int(0)
            kernel32.WriteProcessMemory(h_process,arg_adress,dll_path,dll_len*10,NULL)
            h_kernel32 = win32api.GetModuleHandle("kernel32.dll")
            h_loadlib = win32api.GetProcAddress(h_kernel32, 'LoadLibraryA')
            thread_id = c_ulong(0)
            c_remt = kernel32.CreateRemoteThread(h_process,None,0,h_loadlib,arg_adress,0,byref(thread_id))
            return 1
            if not c_remt:
                return 0