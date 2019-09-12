#pragma once
#include "stdafx.h"
VOID SendTextMessage(wchar_t * wxid, wchar_t * message);
VOID HookWechatQrcode(HWND hwndDlg, DWORD HookAdd);
DWORD GetWeChatWin();