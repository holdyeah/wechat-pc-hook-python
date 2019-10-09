#coding=utf-8
"""
运行前，安装
python -m pip install --upgrade pip
pip install apscheduler,psutil,win32api,ctypes
"""
import os,time
from datetime import datetime
#导入apscheduler线程模块
from apscheduler.schedulers.background import BackgroundScheduler
#导入自定义模块
import tick_read,tick_write,shuju_data,webBaoLiao,webDiQu,hook_wx


def tick_cls():
    os.system('cls')

def tick_claen_readtxt():
    print("清除")
    wx_filename = shuju_data.wechet_lujian+"\\read.txt"
    with open(wx_filename,mode='r+') as f:
        f.seek(0)
        f.truncate()
        f.close()

def tick_make_two_txt():
    #创建两个txt
    wx_filename_read = shuju_data.wechet_lujian+"\\read.txt"
    wx_filename_write = shuju_data.wechet_lujian+"\\write.txt"
    with open(wx_filename_read,mode='w+',encoding="utf-8") as f:
        f.seek(0)
        f.truncate()
        f.close()
    with open(wx_filename_write,mode='w+',encoding="utf-8") as f:
        f.seek(0)
        f.truncate()
        f.close()

#运行
if __name__ == '__main__':
    if hook_wx.hook() == 1:
        scheduler = BackgroundScheduler()
        #初始化
        scheduler.add_job(tick_make_two_txt, 'date', next_run_time=datetime.now())
        # 间隔10秒钟执行一次
        scheduler.add_job(tick_read.tick_read, 'interval', seconds=10, max_instances=1)
        # 间隔10秒钟执行一次
        scheduler.add_job(tick_write.tick_write, 'interval', seconds=10, max_instances=1)
        # 间隔300秒钟执行一次
        scheduler.add_job(tick_cls, 'interval', seconds=300, max_instances=1)
        #间隔一天执行
        scheduler.add_job(tick_claen_readtxt, 'cron', hour=0,minute=3)
        # 这里的调度任务是独立的一个线程
        scheduler.start()
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
        try:
            # 其他任务是独立的线程执行
            while True:
                time.sleep(2)
                if len(shuju_data.piPei_info) > 0:
                    shuju_data.queue.put(webBaoLiao.format_into_a_dictionary_one(shuju_data.piPei_info[0]))
                    shuju_data.piPei_info.pop(0)
                if len(shuju_data.biaoti) > 0:
                    shuju_data.queue.put(webBaoLiao.read_suobe())
                if len(shuju_data.txt_id) > 0:
                    shuju_data.queue.put(webDiQu.write_txt())
                if len(shuju_data.string_cookie) > 0:
                    if len(shuju_data.anti_info) > 0:
                        shuju_data.queue.put(webDiQu.anti())
                        shuju_data.anti_info.pop(0)
        except (KeyboardInterrupt, SystemExit):
            scheduler.shutdown()
            print('Exit The Job!')
    else:
        print("没有找到微信或者微信没有以管理员启动")