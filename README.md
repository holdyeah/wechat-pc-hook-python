# pc微信hook python注入器

hookpc微信客户端的发消息和收信息,运用python自动化收发消息   

基本功能：通过python注入dll到微信中，python筛选数据，转发到某个微信用户或群id,保存聊天记录到read.txt   

微信的版本：   
~~2.6.8.56(2.6.8.56版本发消息call偏移是0x316463)~~   
~~2.7.1.82(2.7.1.82版本发消息call偏移是0x2FA780)~~   
~~2.8.0.133(2.8.0.133版本发消息call偏移是0x32A760)~~  
~~3.0.0.47(3.0.0.47版本发消息call偏移是0x38DAB0)~~  
3.0.0.57(3.0.0.57版本发消息call偏移是0x38D8A0)


开发环境：VS2017使用C++的桌面开发,python3.7.3 32位(备注：64位python可能无法注入dll到微信)   

如何运行：在TeachDemos\Debug\下找到TeachDemos.exe以管理员运行,TeachDemos.exe(默认微信路径是)会加载同目录下的SendMessage.dll到微信中去    

或者修改python_hook.py(python注入器)内的dll_path路径运行python_hook.py 可以注入dll到微信中去    

大神的https://github.com/hedada-hc/pc_wechat_hook    
说明：TeachDemos.exe和微信exe需要以管理员运行，在微信目录下新建三个txt文件，wxid.txt编码UTF-8 write.txt编码UTF-8 read.txt编码UTF-8。不然程序无法读取写入到txt中去(wx_python文件夹不用管，这个是我自己的获取的特定web,收发信息的python)    

内容显示介绍：id/wxid是 wxid_****的一个数据 这个id/wxid 需要通过自己去获取，目前还没有增加到代码里面   
wxid.txt 存放微信id   
发送的内容不需要填写，这个内容写在write.txt中去，dll就能读到发送到wxid去   
大的框是实时信息获取的状态框，内容同时也写入到read.txt中去   
操作方法：先点击获取信息 然后在id/wxid 填写数据 然后点击发送消息即可

# 结构说明

流程图   
![image](https://github.com/holdyeah/wechat-pc-hook-python/blob/master/images/%E8%AF%B4%E6%98%8E.png)   
注入工具 内容显示   
![image](https://github.com/holdyeah/wechat-pc-hook-python/blob/master/images/%E6%A8%A1%E5%9D%97.png)   
