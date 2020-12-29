#pragma once

wchar_t * UTF8ToUnicode(const char* str);
VOID SendTextMessage(wchar_t * wxid, wchar_t * message);
VOID HookWechatRead();