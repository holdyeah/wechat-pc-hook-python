# wechat-pc-hook-python

打算把微信电脑端的发消息的hook加上python自动化   
基本功能：根据python来源获取到特定数据，转发到某个微信id   
微信的版本：2.6.8.56   
开发环境：VS2017 使用C++的桌面开发   
如何运行：在TeachDemos\Debug\下找到TeachDemos.exe以管理员运行,TeachDemos.exe(默认微信路径是)会加载同目录下的SendMessage.dll到微信中去   
大神的https://github.com/hedada-hc/pc_wechat_hook   
说明：TeachDemos.exe和微信exe需要以管理员运行，在微信目录下新建两个txt文件，write.txt编码UTF-8 read.txt编码UTF-8。不然程序无法读取写入到txt中去   

代码和结构非常简陋   
2.6.8.56版本发消息call偏移是0x316463    

web_wx.py不用下载，这个是我自己的获取的特定web,收发信息的python   
流程图   
![image](https://github.com/holdyeah/wechat-pc-hook-python/blob/master/images/%E8%AF%B4%E6%98%8E.png)   
注入工具   
![image](https://github.com/holdyeah/wechat-pc-hook-python/blob/master/images/TeachDemos.png)   
内容显示   
![image](https://github.com/holdyeah/wechat-pc-hook-python/blob/master/images/SendMessage.png)   