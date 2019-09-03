#coding=utf-8
"""
python -m pip install --upgrade pip
pip install apscheduler
"""
import time,os,json,requests,queue
from apscheduler.schedulers.background import BackgroundScheduler


url = 'http://pgc.cloud.nbtv.cn/interfaces/login.do'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/json; charset=UTF-8',
    'Referer': 'http://pgc.cloud.nbtv.cn/tl/login.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
data_search= {
    "account":"ds00502",
    "password":"E10ADC3949BA59ABBE56E057F20F883E"
}

con_url='http://pgc.cloud.nbtv.cn/interfaces/ContentSearch.do'
con_headers = {
    'Accept': '*/*',
    'Content-Type': 'application/json;charset=UTF-8',
    'Referer': 'http://pgc.cloud.nbtv.cn/tl/static/contentManage/allContent.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

session = requests.Session()
queue = queue.Queue()

string_token = []

tonglian_infos_title =[]
tonglian_infos_video =[]
tonglian_infos_area =[]
tonglian_infos_time =[]

read_data_infos_title =[]
read_data_infos_video =[]
read_data_infos_area =[]
read_data_infos_time =[]

def get_token():
    print("获取 token")
    response=session.post(url,headers=headers,data=json.dumps(data_search))
    string_token.append(response.json()['token'])

def get_infos():
    print("获取 infos")
    con_search= {
        "userId":"19",
        "parameter":"",
        "addTimeType":0,
        "starttime":"",
        "endtime":"",
        "contentType":0,
        "newsType":0,
        "initiator":"0",
        "departmentId":"0",
        "pageSize":5,
        "pageNo":1,
        "type":5,
        "token": string_token[0],
    }
    infos_response=session.post(con_url,headers=con_headers,data=json.dumps(con_search),timeout = 20)
    return len(infos_response.json()),infos_response

def decide_infos(infos_response):
    print("判断 infos 是否有新")
    index_data = len(infos_response.json()["pdList"])
    info_title =[]
    info_video =[]
    info_area =[]
    info_time =[]
    data_index = 0
    for index in range(index_data):
        info_title.append(infos_response.json()["pdList"][index]["TITLE"])
        info_video.append(infos_response.json()["pdList"][index]["ATTACHMENTTYPE"])
        info_area.append(infos_response.json()["pdList"][index]["USERNAME"])
        info_time.append(infos_response.json()["pdList"][index]["CREATETIME"])

    if len(tonglian_infos_title):
        print("tonglian_infos_title 里面有值")
        if(tonglian_infos_title[0] == info_title[0]):
            print("判断新的列表跟旧列表第一条是一致的")
        else:
            print("新旧列表第一条不一致")
            #判断有几条不一样的
            for index in range(len(info_title)):
                if(tonglian_infos_title[0] == info_title[index]):
                    data_index += index
            if(data_index == 0):
                print("不用写入到列表")
            else:
                print("写入到列表")
                for index in range(data_index):
                    read_data_infos_title.append(info_title[index])
                    read_data_infos_video.append(info_video[index])
                    read_data_infos_area.append(info_area[index])
                    read_data_infos_time.append(info_time[index])
            #清除tonglian_infos_**  list clear()
            tonglian_infos_title.clear()
            tonglian_infos_video.clear()
            tonglian_infos_area.clear()
            tonglian_infos_time.clear()
            for index in range(index_data):
                tonglian_infos_title.append(infos_response.json()["pdList"][index]["TITLE"])
                tonglian_infos_video.append(infos_response.json()["pdList"][index]["ATTACHMENTTYPE"])
                tonglian_infos_area.append(infos_response.json()["pdList"][index]["USERNAME"])
                tonglian_infos_time.append(infos_response.json()["pdList"][index]["CREATETIME"])

    else:
        print("tonglian_infos_title 里面无值")
        for index in range(index_data):
            tonglian_infos_title.append(infos_response.json()["pdList"][index]["TITLE"])
            tonglian_infos_video.append(infos_response.json()["pdList"][index]["ATTACHMENTTYPE"])
            tonglian_infos_area.append(infos_response.json()["pdList"][index]["USERNAME"])
            tonglian_infos_time.append(infos_response.json()["pdList"][index]["CREATETIME"])

def write_txt():
    print("判断txt写入")
    txt_open = open('C:/Program Files (x86)/Tencent/WeChat/1.txt','r')
    txt = txt_open.read()
    txt_open.close()
    if(txt == ''):
        print("ok了写入")
        data = open('C:/Program Files (x86)/Tencent/WeChat/1.txt','w+')
        txt_data1 = read_data_infos_title[0]
        #判断有没有视频
        txt_data2 = ""
        if read_data_infos_video[0] == '':
            txt_data2 += " 还没有发视频 "
        else:
            txt_data2 += " 有视频 "
        txt_data3 = read_data_infos_area[0]
        txt_data4 = read_data_infos_time[0]
        txt_data1 += txt_data2
        txt_data1 += txt_data3
        txt_data1 += txt_data4
        data.write(txt_data1)
        data.close()
        read_data_infos_title.pop(0)
        read_data_infos_video.pop(0)
        read_data_infos_area.pop(0)
        read_data_infos_time.pop(0)
    else:
        print("txt中有内容")

def tick():
    print("tick")
    if len(string_token):
        print("有 token")
        status_code,infos_response = get_infos()
        if status_code == 3:
            print("token 可以用")
            queue.put(decide_infos(infos_response))

        else:
            print("token 不可以用")
            get_token()
    else:
        print("没有 token，获取token")
        get_token()

def tick1():
    os.system('cls')

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    # 间隔3秒钟执行一次
    scheduler.add_job(tick, 'interval', seconds=3)
    # 间隔300秒钟执行一次
    scheduler.add_job(tick1, 'interval', seconds=300)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        # 其他任务是独立的线程执行
        while True:
            time.sleep(2)
            while len(read_data_infos_title) > 0:
                print('判断txt是否为空,写入到txt文本中去')
                queue.put(write_txt())
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print('Exit The Job!')