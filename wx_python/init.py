#coding=utf-8
"""
运行前，安装
python -m pip install --upgrade pip
pip install apscheduler
"""
import os,time
#导入apscheduler线程模块
from apscheduler.schedulers.background import BackgroundScheduler
#导入自定义模块
import tick_read,tick_write,shuju_data,webBaoLiao,webDiQu


def tick_cls():
    os.system('cls')

def tick_claen_readtxt():
    print("清除")
    wx_filename = "C:\\Program Files (x86)\\Tencent\\WeChat\\read.txt"
    with open(wx_filename,mode='r+') as f:
        f.seek(0)
        f.truncate()
        f.close()

#运行
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
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