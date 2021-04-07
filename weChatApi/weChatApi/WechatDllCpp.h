#pragma once

VOID SendTextMessage(wchar_t * wxid, wchar_t * message);
VOID SendFileMessage(wchar_t * wxid, wchar_t * filepath1);
VOID HookWechatRead();