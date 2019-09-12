# wechat-pc-hook-python

打算把微信电脑端的发消息的hook加上python自动化   
基本功能：根据python来源获取到特定数据，转发到某个微信id   
微信的版本：2.6.8.56   
开发环境：VS2017 使用C++的桌面开发   
大神的https://github.com/hedada-hc/pc_wechat_hook   

代码和结构非常简陋   
发消息call 偏移是 0x316463   
需要在微信目录下新建两个txt文件，write.txt编码ASNI read.txt编码UTF-8   
流程图   
![image](https://github.com/holdyeah/wechat-pc-hook-python/blob/master/images/%E8%AF%B4%E6%98%8E.png)   
注入工具   
![image](https://github.com/holdyeah/wechat-pc-hook-python/blob/master/images/TeachDemos.png)   
内容显示   
![image](https://github.com/holdyeah/wechat-pc-hook-python/blob/master/images/SendMessage.png)   