// dllmain.cpp : 定义 DLL 应用程序的入口点。
#include "pch.h"
#include <stdio.h>
#include "WechatDllCpp.h"
#include "httpServer.h"

DWORD ThreadProc_http();
DWORD ThreadProc_redis();
DWORD ThreadProc_read();

BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
		CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)ThreadProc_http, hModule, 0, NULL);
		CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)ThreadProc_read, hModule, 0, NULL);
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

DWORD ThreadProc_redis()
{
	return 0;
}

DWORD ThreadProc_http()
{
	httpServer();
	return TRUE;
}


DWORD ThreadProc_read()
{
	HookWechatRead();
	return TRUE;
}