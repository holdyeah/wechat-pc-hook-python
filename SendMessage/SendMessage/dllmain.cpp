// dllmain.cpp : 定义 DLL 应用程序的入口点。
#include "stdafx.h"
#include <Windows.h>
#include "resource.h"
#include "SendMessage.h"
DWORD ThreadProc(HMODULE hModule);
INT_PTR CALLBACK DialogProc(_In_ HWND hwndDlg, _In_ UINT uMsg, _In_ WPARAM wParam, _In_ LPARAM lParam);
BOOL RegisterWindow(HMODULE hModule);
INT isbool = 0;
wchar_t wxid[0x100] = { 0 };
wchar_t message[0x300] = { 0 };

BOOL APIENTRY DllMain(HMODULE hModule,
	DWORD  ul_reason_for_call,
	LPVOID lpReserved
)
{
	switch (ul_reason_for_call)
	{
	case DLL_PROCESS_ATTACH:
		//启动一个线程
		CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)ThreadProc, hModule, 0, NULL);
		//启动一个线程
		CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)RegisterWindow, hModule, 0, NULL);
	case DLL_THREAD_ATTACH:
	case DLL_THREAD_DETACH:
	case DLL_PROCESS_DETACH:
		break;
	}
	return TRUE;
}

DWORD ThreadProc(HMODULE hModule)
{
	DialogBox(hModule, MAKEINTRESOURCE(MAIN), NULL, DialogProc);
	return TRUE;
}

INT_PTR CALLBACK DialogProc(_In_ HWND hwndDlg, _In_ UINT uMsg, _In_ WPARAM wParam, _In_ LPARAM lParam)
{	
	DWORD hookAdd = GetWeChatWin() + 0x316463;
	switch (uMsg)
	{
	case WM_INITDIALOG:
		break;
	case WM_CLOSE:
		EndDialog(hwndDlg, 0);
		break;
	case WM_COMMAND:
		if (wParam == SEND)
		{
			isbool = 0;
			isbool++;
			GetDlgItemText(hwndDlg, WXID, wxid, sizeof(wxid));
			GetDlgItemText(hwndDlg, MESSAGE, message, sizeof(message));
			//SendTextMessage(wxid, message);
		}
		if (wParam == ID_STOP)
		{
			isbool--;
			wxid == 0;
			message == 0;
			//SendTextMessage(wxid, message);
		}
		if (wParam == RECV) {
			//MessageBox(NULL, L"到了", L"哈哈", 0);
			HookWechatQrcode(hwndDlg, hookAdd);
		}
		break;
	default:
		break;
	}
	return FALSE;
}

BOOL RegisterWindow(HMODULE hModule)
{
	while (TRUE)
	{
		if (isbool >= 1)
		{
			SendTextMessage(wxid, message);
			Sleep(50000);
			//MessageBox(NULL, L"test", L"错误", 0);
		}
		
	}

	return FALSE;
}