#coding=utf-8
"""
python -m pip install --upgrade pip
pip install apscheduler
"""
import time,os
from apscheduler.schedulers.background import BackgroundScheduler

def tick():
    print("tick")

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    # 间隔3秒钟执行一次
    scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        # 其他任务是独立的线程执行
        while True:
            time.sleep(2)
            print('sleep!')
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print('Exit The Job!')