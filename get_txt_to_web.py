#coding=utf-8
"""
python -m pip install --upgrade pip
pip install apscheduler
"""
import time,os,shutil,re,queue,requests,json,urllib.request
from apscheduler.schedulers.background import BackgroundScheduler
from requests.packages import urllib3
from urllib.parse import urlencode
from bs4 import BeautifulSoup

urllib3.disable_warnings()  #从urllib3中消除警告
session = requests.Session()
queue = queue.Queue()
old_results_number = [0]
results_info =[]

def copy_wx_file(wx_filename,copy_filename):
    newstime = time.strftime('%Y-%m-%d',time.localtime())
    shutil.copy(wx_filename,copy_filename+newstime+'.txt')

def screening_data(filename):
    TXTtemp = open(filename,encoding='utf-8')
    txtbuffer=TXTtemp.read()
    strlist1=txtbuffer.replace("\n"," ")
    findword =u"(#.*?&)"
    pattern = re.compile(findword)
    results = pattern.findall(strlist1)
    return results,len(results)

def format_into_a_dictionary_one(into):
    into_data = into
    lists = []
    size_up_number = []
    newstime = time.strftime('%Y%m%d',time.localtime())
    wu  = into_data.find('#')
    wu_time  = into_data.find(newstime)
    fen_hao  = into_data.find('：')
    one      = into_data.find('1、')
    two      = into_data.find('2、')
    three    = into_data.find('3、')
    four     = into_data.find('4、')
    five     = into_data.find('5、')
    six      = into_data.find('6、')
    seven    = into_data.find('7、')
    eight    = into_data.find('8、')
    nine     = into_data.find('9、')
    ten      = into_data.find('10、')
    eleven   = into_data.find('11、')
    twelve   = into_data.find('12、')
    thirteen = into_data.find('13、')
    fourteen = into_data.find('14、')
    fifteen  = into_data.find('15、')
    sixteen  = into_data.find('16、')
    seveteen = into_data.find('17、')
    eighteen = into_data.find('18、')
    nineteen = into_data.find('19、')
    size_up_number.append(one)
    size_up_number.append(two)
    size_up_number.append(three)
    size_up_number.append(four)
    size_up_number.append(five)
    size_up_number.append(six)
    size_up_number.append(seven)
    size_up_number.append(eight)
    size_up_number.append(nine)
    size_up_number.append(ten)
    size_up_number.append(eleven)
    size_up_number.append(twelve)
    size_up_number.append(thirteen)
    size_up_number.append(fourteen)
    size_up_number.append(fifteen)
    size_up_number.append(sixteen)
    size_up_number.append(seveteen)
    size_up_number.append(eighteen)
    size_up_number.append(nineteen)
    size_up_number.append(wu)
    size_up_number.append(wu_time)
    size_up_number.append(fen_hao)
    title = into_data[size_up_number[19]+1:size_up_number[21]]
    number = -1
    index_number = size_up_number.index(number)
    for index in range(index_number):
        str0 = into_data[size_up_number[index]:size_up_number[index+1]]
        lists.append(str0)
    return title,lists

def user(suobe_title):
    txt_title = suobe_title
    if txt_title.find("test") != -1:
        return 'ds*****','******'
    elif txt_title.find("test1") != -1:
        return 'ds*****','******','test1'
    elif txt_title.find("test1") != -1:
        return 'ds*****','******','test1'
    else:
        return 'ds*****','******','test'

def run_results_number(results,old_results_number,news_results_number):
    print("扫描文件有无新内容")
    print("当前文件内一共有: " +str(news_results_number) + " 条内容")
    if news_results_number-old_results_number[0] ==0:
        print("无新内容")
        old_results_number[0] = news_results_number
    else:
        print("有新内容,添加入库")
        increase_results_number =[0]
        increase_results_number[0] = news_results_number-old_results_number[0]
        for index_number in range(increase_results_number[0]):
            info = results[old_results_number[0]+index_number]
            results_info.append(info)
        old_results_number[0] = news_results_number

def check_network():
    res_network = session.get("******",verify=False)
    return res_network.status_code

def open_chrme(username,userpass,column,info_lists):
    time.sleep(1)
    while True:
        session = requests.Session()
        time.sleep(2)
        login_cookies = ''
        login_lt=''
        login_strTemp=''
        login_e1s2=''
        respon_get = session.get("******",verify=False)
        cookies = requests.utils.dict_from_cookiejar(respon_get.cookies)
        login_cookies = login_cookies+'JSESSIONID='+cookies['JSESSIONID']
        login_html=BeautifulSoup(respon_get.text,'lxml')
        lt =login_html.find_all('input',attrs = {'name' : 'lt'})
        strTemp =login_html.find_all('input',attrs = {'name' : 'strTemp'})
        ltlt =login_html.find_all('input',attrs = {'name' : 'execution'})
        for k in lt:
            login_lt = (k['value'])
        for k in strTemp:
            login_strTemp =(k['value'])
        for k in ltlt:
            login_e1s2 =(k['value'])
        print(login_cookies)   
        login_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': login_cookies,
            'Host': '******',
            'Origin': '******',
            'Referer': '******',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        }
        login_data='username='+username+'&strTemp='+login_strTemp+'&password='+userpass+'&lt='+login_lt+'&execution='+login_e1s2+'&_eventId=submit&submit=%E7%AB%8B%E5%8D%B3%E7%99%BB%E5%BD%95'
        login_url = '******'
        login_response=session.post(login_url,headers=login_headers,data=login_data,verify=False)
        print(login_response.status_code)
        if login_response.status_code != 200:
            print("登录失败")
            time.sleep(10)
            continue
        elif login_response.status_code == 200:
            print("登录成功")
            time.sleep(2)
            url_ecc='http://******/portal/Login/loginCas;jsessionid='+session.cookies['JSESSIONID']+'?key=menu_bl'
            ecc_get = session.get(url_ecc,verify=False)
            ecc_token ='siteCode=S1; token='+ecc_get.url[69:]
            ecc_headers ={
                'Accept':'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': '******',
                'Connection': 'keep-alive',
                'Origin': '://****/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                'Content-Type': 'application/json;charset=UTF-8',
                'Referer': '://****/',
                "Referrer Policy":"no-referrer-when-downgrade",
                'Cookie': ecc_token,
            }
            print(len(info_lists))
            for index in range(len(info_lists)):
                info_size_up_number =[]
                info_str = info_lists[index]
                dun_hao     = info_str.find('、')
                fu_place    = info_str.find('地点')
                fu_reporter = info_str.find('记者')
                fu_content  = info_str.find('内容')
                info_size_up_number.append(info_str)
                info_size_up_number.append(fu_place)
                info_size_up_number.append(fu_reporter)
                info_size_up_number.append(fu_content)
                title_info = (info_str[dun_hao+1:fu_place])
                place = (info_str[fu_place+3:fu_reporter])
                reporter = (info_str[fu_reporter+3:fu_content])
                content = (info_str[fu_content+3:])
                columnCode = ""
                columnname = ""
                if column == "test":
                    columnCode = "test"
                    columnname = "test"
                else:
                    columnCode = "test"
                    columnname = "test"
                description = content
                title = title_info
                createUserName = "test"
                siteName  = "test"
                data_ecc ='''{\"strategy\":{\"send\":true,\"task\":false},\"columnCode\":\"'''+columnCode+'''\",\"description\":\"<p>'''+description+'''</p>\",\"source\":\"4\",\"category\":\"1\",\"title\":\"'''+title+'''\",\"phone\":\"test\",\"clueCreateTime\":null,\"columnname\":\"'''+columnname +'''\",\"createUserCode\":\"6E76\",\"createUserName\":\"'''+createUserName+'''\",\"siteCode\":\"S1\",\"siteName\":\"'''+ siteName +'''\"}'''
                print(data_ecc)
                url_ecc_post='http://****/tpp/rest/content/clue/add'
                response_ecc=session.post(url_ecc_post,data=data_ecc.encode('utf-8'),headers=ecc_headers,verify=False)
                print(response_ecc.json())
                
            print("hook")
            break
            
def read_suobe(username,userpass,column,suobe_lists):
    print("入库的是: "+column+" 栏目")
    name = username
    password = userpass
    info_column = column
    info_lists = suobe_lists
    time.sleep(2)
    while True:
        driver_status_code = check_network()
        if driver_status_code != 200:
            print("网络错误")
            time.sleep(150)
            continue
        elif driver_status_code == 200:
            print("网络正常")
            open_chrme(name,password,info_column,info_lists)
            print("=======")
            break
    print("关闭")

def tick():
    print("开始")
    wx_filename = 'C:\\Program Files (x86)\\Tencent\\WeChat\\read.txt'
    copy_filename = 'C:\\Users\\wx\\Desktop\\wx\\raw_data\\'
    copy_wx_file(wx_filename,copy_filename)
    newstime = time.strftime('%Y-%m-%d',time.localtime())
    results,news_results_number = screening_data(copy_filename+newstime+'.txt')
    run_results_number(results,old_results_number,news_results_number)
def tick1():
    print("清除")
    wx_filename = "C:\\Program Files (x86)\\Tencent\\WeChat\\read.txt"
    with open(wx_filename,encoding='utf-8',mode='r+') as f:
        f.seek(0)
        f.truncate()
        f.close()
if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick,'interval', seconds=20,max_instances=1)
    scheduler.add_job(tick1, 'cron', hour=0,minute=3)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        # 其他任务是独立的线程执行
        while True:
            time.sleep(2)
            while len(results_info) > 0:
                suobe_title,suobe_lists = format_into_a_dictionary_one(results_info[0])
                username,userpass,column =user(suobe_title)
                queue.put(read_suobe(username,userpass,column,suobe_lists))
                results_info.pop(0)                
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print('Exit The Job!')