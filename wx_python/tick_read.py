#coding=utf-8
import os,time
import shuju_data,webBaoLiao
def tick_read():
    print('扫描微信read.txt内是否有匹配的数据')
    #微信read.txt目录
    wx_filename = 'C:\\Program Files (x86)\\Tencent\\WeChat\\read.txt'
    #获取当前工作的父目录 的raw_data目录
    copy_filename = os.path.abspath('.') + '\\raw_data\\'
    #复制read.txt到cpoy_filename路径
    webBaoLiao.copy_wx_file_to_cpyefilename(wx_filename,copy_filename)
    #newstime格式是2000-01-01
    newstime = time.strftime('%Y-%m-%d',time.localtime())
    PiPei_data,PiPei_number,anti_data,anti_number = webBaoLiao.screening_txtData(copy_filename+newstime+'.txt')
    #查询PiPei是否有新内容,有就加入到piPei_info列表中去
    webBaoLiao.run_results_number(shuju_data.pipei,PiPei_data,shuju_data.old_PiPei_number,PiPei_number,shuju_data.piPei_info)
    #查询anti是否有新内容,有就加入到anti_info列表中去
    webBaoLiao.run_results_number(shuju_data.anti,anti_data,shuju_data.old_anti_number,anti_number,shuju_data.anti_info)