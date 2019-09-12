// SendMessage.cpp : 定义 DLL 应用程序的导出函数。
//

#include "stdafx.h"
#include <Windows.h>
#include <stdio.h>
#include "resource.h"
#define HOOK_LEN 5
HANDLE hWHND = 0;
BYTE backCode[HOOK_LEN] = { 0 };
DWORD hookData = 0;
DWORD WinAdd = 0;
DWORD retCallAdd = 0;
DWORD retAdd = 0;
HWND hDlg = 0;


struct wxStr
{
	wchar_t * pStr;
	int strLen;
	int strLen2;
};
//获取wechatWin模块
DWORD GetWeChatWin()
{
	return (DWORD)LoadLibrary(L"WeChatWin.dll");
}
//发送文本信息
VOID SendTextMessage(wchar_t * wxid, wchar_t * message)
{
	//发送消息call 2DA0F0
	DWORD sendCall = GetWeChatWin() + 0x2EBAA0;

	wxStr pWxid = {0};
	pWxid.pStr = wxid;
	pWxid.strLen = wcslen(wxid);
	pWxid.strLen2 = wcslen(wxid)* 2;

	wxStr pMessage = { 0 };
	pMessage.pStr = message;
	pMessage.strLen = wcslen(message);
	pMessage.strLen2 = wcslen(message) * 2;
	//取地址
	char * asmWxid = (char *)&pWxid.pStr;
	char * asmMessage = (char *)&pMessage.pStr;

	char buff[0x880] = { 0 };
	__asm 
	{
		mov edx, asmWxid;
		push 0x1;
		mov eax, 0x0;
		push eax;
		mov ebx, asmMessage;
		push ebx;
		lea ecx, buff;
		call sendCall;
		add esp, 0xC;
	}
}





//test
/*
esi + 0x178 消息内容
esi + 0x1A0 如果是个人消息则是个人wxid如果是群消息则是群id
esi + 0xCC 如果是群消息则这里为群里发送消息人的wxid反之为0x0
*/
//显示数据
VOID printLog(DWORD msgAdd)
{
	DWORD wxidAdd = msgAdd - 0x1A0;
	DWORD wxid2Add = msgAdd - 0xCC;
	DWORD messageAdd = msgAdd - 0x178;
	wchar_t wxid[0x100] = { 0 };
	wchar_t wxid2[0x100] = { 0 };
	wchar_t message[] = { 0 };
	TCHAR buff[0x8000] = { 0 };
	GetDlgItemText(hDlg, MESSAGE_LOG, buff, sizeof(buff));
	if (*(LPVOID *)wxid2Add <= 0x0) {
		swprintf_s(buff, L"%s wxid:%s 消息内容:%s\r\n", buff, *((LPVOID *)wxidAdd), *((LPVOID *)messageAdd));
		//swprintf_s(buff, L"ESI=%p wxid=%p wxid2=%p wxid2=%p\r\n", msgAdd, msgAdd - 0x1A0, *((LPVOID *)wxidAdd));
	}
	else {
		swprintf_s(buff, L"%s 群ID:%s 发送者ID:%s 消息内容:%s\r\n", buff, *((LPVOID *)wxidAdd), *((LPVOID *)wxid2Add), *((LPVOID *)messageAdd));
	}

	SetDlgItemText(hDlg, MESSAGE_LOG, buff);
}

DWORD cEax = 0;
DWORD cEcx = 0;
DWORD cEdx = 0;
DWORD cEbx = 0;
DWORD cEsp = 0;
DWORD cEbp = 0;
DWORD cEsi = 0;
DWORD cEdi = 0;
DWORD retCallAdd2 = 0;
//跳转过来的函数 我们自己的
VOID __declspec(naked) HookF()
{
	//pushad: 将所有的32位通用寄存器压入堆栈
	//pushfd:然后将32位标志寄存器EFLAGS压入堆栈
	//popad:将所有的32位通用寄存器取出堆栈
	//popfd:将32位标志寄存器EFLAGS取出堆栈
	//先保存寄存器
	// 使用pushad这些来搞还是不太稳定  还是用变量把寄存器的值保存下来 这样可靠点
	__asm {
		mov cEax, eax
		mov cEcx, ecx
		mov cEdx, edx
		mov cEbx, ebx
		mov cEsp, esp
		mov cEbp, ebp
		mov cEsi, esi
		mov cEdi, edi

		pushad
		pushfd
	}
	//然后跳转到我们自己的处理函数 想干嘛干嘛
	printLog(cEsi);
	retCallAdd = WinAdd + 0x126D7D8;
	retCallAdd2 = WinAdd + 0x259E90;
	retAdd = WinAdd + 0x316468;
	//然后在还原他进来之前的所有数据
	/*popad
		popfd  不太可靠恢复不全 所以才有变量的方式保存下来再赋值过去*/
	__asm {
		/*mov eax, cEax
		mov ecx, cEcx
		mov edx, cEdx
		mov ebx, cEbx
		mov esp, cEsp
		mov ebp, cEbp
		mov esi, cEsi
		mov edi, cEdi
		mov eax, retCallAdd
		call retCallAdd2*/
		popfd
		popad
		jmp retAdd
	}
}

VOID StartHook(DWORD hookAdd, LPVOID jmpAdd)
{
	BYTE JmpCode[HOOK_LEN] = { 0 };
	//我们需要组成一段这样的数据
	// E9 11051111(这里是跳转的地方这个地方不是一个代码地址 而是根据hook地址和跳转的代码地址的距离计算出来的)
	JmpCode[0] = 0xE9;
	//计算跳转的距离公式是固定的
	//计算公式为 跳转的地址(也就是我们函数的地址) - hook的地址 - hook的字节长度
	*(DWORD *)&JmpCode[1] = (DWORD)jmpAdd - hookAdd - HOOK_LEN;

	//hook第二步 先备份将要被我们覆盖地址的数据 长度为我们hook的长度 HOOK_LEN 5个字节

	//获取进程句柄

	wchar_t debugBuff[0x100] = { 0 };
	swprintf_s(debugBuff, L"hook地址=%p  进程句柄=%p  jmp函数=%p  AA=%p", hookAdd, hWHND, jmpAdd, &HookF);
	MessageBox(NULL, debugBuff, L"测试", MB_OK);
	//备份数据
	if (ReadProcessMemory(hWHND, (LPVOID)hookAdd, backCode, HOOK_LEN, NULL) == 0) {

		swprintf_s(debugBuff, L"hook地址=%p  进程句柄=%p  错误类型=%d", hookAdd, hWHND, GetLastError());
		MessageBox(NULL, debugBuff, L"读取失败", MB_OK);
		//MessageBox(NULL,"hook地址的数据读取失败","读取失败",MB_OK);
		return;
	}

	//真正的hook开始了 把我们要替换的函数地址写进去 让他直接跳到我们函数里面去然后我们处理完毕后再放行吧！
	if (WriteProcessMemory(hWHND, (LPVOID)hookAdd, JmpCode, HOOK_LEN, NULL) == 0) {
		MessageBox(NULL, L"hook写入失败，函数替换失败", L"错误", MB_OK);
		return;
	}
	MessageBox(NULL, L"成功HOOK", L"成功", MB_OK);
}





//
VOID HookWechatQrcode(HWND hwndDlg, DWORD HookAdd)
{
	hWHND = OpenProcess(PROCESS_ALL_ACCESS, NULL, GetCurrentProcessId());
	WinAdd = GetWeChatWin();
	hDlg = hwndDlg;
	StartHook(HookAdd, &HookF);
}
