#coding=utf-8
"""
运行前，安装
python -m pip install --upgrade pip
pip install apscheduler

"""
import os,time,shutil,re,queue,requests,json,random
#导入apscheduler线程模块
from apscheduler.schedulers.background import BackgroundScheduler
from requests.packages import urllib3
from urllib.parse import urlencode
from bs4 import BeautifulSoup

#从urllib3中消除警告
urllib3.disable_warnings()  
session = requests.Session()
#队列
queue = queue.Queue()

#检查web是否正常
def check_network():
    res_network = session.get("https://cas.*****.cn/login?service=http%3A%2F%2Fweb.*****.cn%2Flogin%2Fmain%2F",verify=False)
    return res_network.status_code

#web爆料
def open_chrme_webBaoLiao(username,userpass,column,info_lists):
    time.sleep(1)
    while True:
        session = requests.Session()
        time.sleep(2)
        login_cookies = ''
        login_lt=''
        login_strTemp=''
        login_e1s2=''
        respon_get = session.get("https://cas.*****.cn/login?service=http%3A%2F%2Fweb.*****.cn%2Flogin%2Fmain%2F",verify=False)
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
        login_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': login_cookies,
            'Host': 'cas.*****.cn',
            'Origin': 'https://cas.*****.cn',
            'Referer': 'https://cas.*****.cn/login?service=http%3A%2F%2Fweb.*****.cn%2Flogin%2Fmain%2F',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        }
        login_data='username='+username+'&strTemp='+login_strTemp+'&password='+userpass+'&lt='+login_lt+'&execution='+login_e1s2+'&_eventId=submit&submit=%E7%AB%8B%E5%8D%B3%E7%99%BB%E5%BD%95'
        login_url = 'https://cas.*****.cn/login?service=http%3A%2F%2Fweb.*****.cn%2Flogin%2Fmain%2F'
        login_response=session.post(login_url,headers=login_headers,data=login_data,verify=False)
        print(login_response.status_code)
        if login_response.status_code != 200:
            print("登录失败")
            time.sleep(10)
            continue
        elif login_response.status_code == 200:
            print("登录成功")
            time.sleep(2)
            url_ecc='http://ecc.*****.cn:19207/portal/Login/loginCas;jsessionid='+session.cookies['JSESSIONID']+'?key=menu_bl'
            ecc_get = session.get(url_ecc,verify=False)
            ecc_token ='siteCode=S1; token='+ecc_get.url[69:]
            ecc_headers ={
                'Accept':'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'ecc.*****.cn:19207',
                'Connection': 'keep-alive',
                'Origin': 'http://ecc.*****.cn:19207',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                'Content-Type': 'application/json;charset=UTF-8',
                'Referer': 'http://ecc.*****.cn:19207/tpp/',
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
                if column == ".*****.":
                    columnCode = ".*****."
                    columnname = ".*****."
                elif column == ".*****.":
                    columnCode = ".*****."
                    columnname = ".*****."
                elif column == ".*****.":
                    columnCode = ".*****."
                    columnname = ".*****."
                elif column == ".*****.":
                    columnCode = ".*****."
                    columnname = ".*****."
                else:
                    columnCode = ".*****."
                    columnname = ".*****."
                description = content
                title = title_info
                createUserName = ".*****."
                siteName  = ".*****."
                data_ecc ='''{\"strategy\":{\"send\":true,\"task\":false},\"columnCode\":\"'''+columnCode+'''\",\"description\":\"<p>'''+description+'''</p>\",\"source\":\"4\",\"category\":\"1\",\"title\":\"'''+title+'''\",\"phone\":\"test\",\"clueCreateTime\":null,\"columnname\":\"'''+columnname +'''\",\"createUserCode\":\"6E76\",\"createUserName\":\"'''+createUserName+'''\",\"siteCode\":\"S1\",\"siteName\":\"'''+ siteName +'''\"}'''
                print(data_ecc)
                url_ecc_post='http://ecc.*****.cn:19207/tpp/rest/content/clue/add'
                response_ecc=session.post(url_ecc_post,data=data_ecc.encode('utf-8'),headers=ecc_headers,verify=False)
                #print(response_ecc.json())
                uuid = response_ecc.json()['data'][0]['uuid']
                uuid_url = 'http://ecc.*****.cn:19207/tpp/rest/content/clue/updateStatus?uuid='+uuid
                headers_uuid ={
                    'Accept':'application/json, text/plain, */*',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Host': 'ecc.*****.cn:19207',
                    'Connection': 'keep-alive',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Referer': 'http://ecc.*****.cn:19207/tpp/',
                    'Cookie': ecc_token,
                }
                response_uuid=session.get(uuid_url,headers=headers_uuid,verify=False)
                print(response_uuid.json())
                
            print("hook")
            break

#内容写入到web爆料中
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
            open_chrme_webBaoLiao(name,password,info_column,info_lists)
            print("=======")
            break
    print("关闭")

"""
从read.txt中获取到实时数据信息
判断是否是自己需要的内容
是自己需要的内容就一条一条的写入到web爆料中去
"""
#旧的条目长度
old_results_number = [0]
#内容
results_info =[]
#格式化内容返回标题和内容
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

#根据标题返回不同账号
def user(suobe_title):
    txt_title = suobe_title
    if txt_title.find(".*****.") != -1:
        return '.*****.','.*****.','.*****.'
    elif txt_title.find(".*****.") != -1:
        return '.*****.','.*****.','.*****.'
    elif txt_title.find(".*****.") != -1:
        return '.*****.','.*****.','.*****.'
    else:
        return '.*****.','.*****.','.*****.'

#复制文本到命名为2000-01-01.txt格式 copy_filename路径下
def copy_wx_file_to_cpyefilename(wx_filename,copy_filename):
    newstime = time.strftime('%Y-%m-%d',time.localtime())
    shutil.copy(wx_filename,copy_filename+newstime+'.txt')

#扫描txt内容匹配开头是#结尾是&的内容，返回指定内容和条数
def screening_txtData(filename):
    TXTtemp = open(filename,encoding='utf-8')
    txtbuffer=TXTtemp.read()
    strlist1=txtbuffer.replace("\n"," ")
    findword =u"(#.*?&)"
    pattern = re.compile(findword)
    results = pattern.findall(strlist1)
    return results,len(results)

#检查新的扫描内容，跟旧的内容是否一致，是则不变，否则增加新内容到results_info
def run_results_number(results,old_results_number,news_results_number):
    print("当前扫描文件内一共有: " +str(news_results_number) + " 条内容")
    if news_results_number-old_results_number[0] ==0:
        print("无新增内容")
        old_results_number[0] = news_results_number
    else:
        print("扫描到有新内容,添加到results_info成功")
        increase_results_number =[0]
        increase_results_number[0] = news_results_number-old_results_number[0]
        for index_number in range(increase_results_number[0]):
            info = results[old_results_number[0]+index_number]
            results_info.append(info) 
        old_results_number[0] = news_results_number

def tick_go_read_to_webBaoLiao():
    print('获取read.txt中相关信息写入到web爆料!')
    #微信read.txt目录
    wx_filename = 'C:\\Program Files (x86)\\Tencent\\WeChat\\read.txt'
    copy_filename = 'C:\\Users\\wx\\Desktop\\wx\\raw_data\\'
    #复制read.txt到cpoy_filename路径
    copy_wx_file_to_cpyefilename(wx_filename,copy_filename)
    #newstime 2000-01-01
    newstime = time.strftime('%Y-%m-%d',time.localtime())
    results_PiPei_data,news_results_number = screening_txtData(copy_filename+newstime+'.txt')
    run_results_number(results_PiPei_data,old_results_number,news_results_number)


"""
实时读取webxx地区信息
判断是否有新信息条目
有新就一条一条的发送到微信和写入到web爆料中
"""
#列表是读取到的内容列表
tonglian_infos_title =[]
tonglian_infos_video =[]
tonglian_infos_area =[]
tonglian_infos_time =[]
#需求写入txt的列表
read_data_infos_title =[]
read_data_infos_video =[]
read_data_infos_area =[]
read_data_infos_time =[]
#需求写入web爆料的列表
read_data_Webinfos_title =[]
read_data_Webinfos_video =[]
read_data_Webinfos_area =[]
read_data_Webinfos_time =[]
#登录的token
string_token = []
string_ID = []
#获取登录token地址
url = 'http://pgc.*****.cn/interfaces/login.do'
#登录的头文件
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/json; charset=UTF-8',
    'Referer': 'http://pgc.*****.cn/tl/login.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
#登录账号密码
data_search= [
    {'account':'.*****.','password':'.*****.'},
    {'account':'.*****.','password':'.*****.'},
    {'account':'.*****.','password':'.*****.'},
    {'account':'.*****.','password':'.*****.'},
    {'account':'.*****.','password':'.*****.'},
    {'account':'.*****.','password':'.*****.'},
    {'account':'.*****.','password':'.*****.'},
    {'account':'.*****.','password':'.*****.'},
    {'account':'.*****.','password':'.*****.'},
    {'account':'.*****.','password':'.*****.'},
]
#获取内容地址
con_url='http://pgc.*****.cn/interfaces/ContentSearch.do'
#获取内容的头
con_headers = {
    'Accept': '*/*',
    'Content-Type': 'application/json;charset=UTF-8',
    'Referer': 'http://pgc..*****.cn/tl/static/contentManage/allContent.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

#web爆料来源是web地区
def open_chrme_webBaoLiao_toDaiQu(username,userpass):
    time.sleep(1)
    while True:
        session = requests.Session()
        time.sleep(2)
        login_cookies = ''
        login_lt=''
        login_strTemp=''
        login_e1s2=''
        respon_get = session.get("https://cas.*****.cn/login?service=http%3A%2F%2Fweb.*****.cn%2Flogin%2Fmain%2F",verify=False)
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
        login_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': login_cookies,
            'Host': 'cas.*****.cn',
            'Origin': 'https://cas.*****.cn',
            'Referer': 'https://cas.*****.cn/login?service=http%3A%2F%2Fweb.*****.cn%2Flogin%2Fmain%2F',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        }
        login_data='username='+username+'&strTemp='+login_strTemp+'&password='+userpass+'&lt='+login_lt+'&execution='+login_e1s2+'&_eventId=submit&submit=%E7%AB%8B%E5%8D%B3%E7%99%BB%E5%BD%95'
        login_url = 'https://cas.*****.cn/login?service=http%3A%2F%2Fweb.*****.cn%2Flogin%2Fmain%2F'
        login_response=session.post(login_url,headers=login_headers,data=login_data,verify=False)
        print(login_response.status_code)
        if login_response.status_code != 200:
            print("登录失败")
            time.sleep(10)
            continue
        elif login_response.status_code == 200:
            print("登录成功")
            time.sleep(2)
            url_ecc='http://ecc.*****.cn:19207/portal/Login/loginCas;jsessionid='+session.cookies['JSESSIONID']+'?key=menu_bl'
            ecc_get = session.get(url_ecc,verify=False)
            ecc_token ='siteCode=S1; token='+ecc_get.url[69:]
            ecc_headers ={
                'Accept':'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'ecc.*****.cn:19207',
                'Connection': 'keep-alive',
                'Origin': 'http://ecc.*****.cn:19207',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                'Content-Type': 'application/json;charset=UTF-8',
                'Referer': 'http://ecc.*****.cn:19207/tpp/',
                "Referrer Policy":"no-referrer-when-downgrade",
                'Cookie': ecc_token,
            }
            columnCode = ".*****."
            columnname = ".*****."
            description = read_data_Webinfos_title[0]
            title = read_data_Webinfos_title[0]
            createUserName = ".*****."
            siteName  = ".*****."
            data_ecc ='''{\"strategy\":{\"send\":true,\"task\":false},\"columnCode\":\"'''+columnCode+'''\",\"description\":\"<p>'''+description+'''</p>\",\"source\":\"4\",\"category\":\"1\",\"title\":\"'''+title+'''\",\"phone\":\"test\",\"clueCreateTime\":null,\"columnname\":\"'''+columnname +'''\",\"createUserCode\":\"6E76\",\"createUserName\":\"'''+createUserName+'''\",\"siteCode\":\"S1\",\"siteName\":\"'''+ siteName +'''\"}'''
            url_ecc_post='http://ecc.*****.cn:19207/tpp/rest/content/clue/add'
            response_ecc=session.post(url_ecc_post,data=data_ecc.encode('utf-8'),headers=ecc_headers,verify=False)
            uuid = response_ecc.json()['data'][0]['uuid']
            uuid_url = 'http://ecc.*****.cn:19207/tpp/rest/content/clue/updateStatus?uuid='+uuid
            headers_uuid ={
                'Accept':'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'ecc.*****.cn:19207',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                'Content-Type': 'application/json;charset=UTF-8',
                'Referer': 'http://ecc.*****.cn:19207/tpp/',
                'Cookie': ecc_token,
            }
            response_uuid=session.get(uuid_url,headers=headers_uuid,verify=False)
            print(response_uuid.json())
            print("hook")
            break

#随机获取data_search其中一个数登录获取token
def get_token():
    print("获取 token")
    data_nmber = len(data_search)-1
    ran = random.randint(0,data_nmber)
    print(ran)
    print(data_search[ran])
    response=session.post(url,headers=headers,data=json.dumps(data_search[ran]))
    string_token.append(response.json()['token'])
    string_ID.append(response.json()['ID'])

#post获取信息，返回长度和内容
def get_infos():
    print("获取 infos")
    con_search= {
        "userId":string_ID[0],
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

#判断内容是否有新
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
                    read_data_Webinfos_title.append(info_title[index])
                    read_data_Webinfos_video.append(info_video[index])
                    read_data_Webinfos_area.append(info_area[index])
                    read_data_Webinfos_time.append(info_time[index])
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

#判断write.txt是否有内容，无则写入一条内容，有则不写入
def write_txt():
    print("判断txt写入")
    txt_open = open('C:/Program Files (x86)/Tencent/WeChat/write.txt','r')
    txt = txt_open.read()
    txt_open.close()
    if(txt == ''):
        print("ok了写入")
        data = open('C:/Program Files (x86)/Tencent/WeChat/write.txt','w+')
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
        print("txt中有内容，不写入，等待")

#内容写入到web爆料中
def read_suobe_BaoLiao():
    name = '.*****.'
    password = '.*****.'
    time.sleep(2)
    while True:
        driver_status_code = check_network()
        if driver_status_code != 200:
            print("网络错误")
            time.sleep(150)
            continue
        elif driver_status_code == 200:
            print("网络正常")
            open_chrme_webBaoLiao_toDaiQu(name,password)
            print("=======")
            break
    print("关闭")


def tick_go_webDiQu_to_wx_and_webBaoLiao():
    print('获取web地区新条目发送到微信和写入到web爆料!')
    if len(string_token):
        print("有 token")
        status_code,infos_response = get_infos()
        if status_code == 3:
            print("token 可以用")
            queue.put(decide_infos(infos_response))

        else:
            print("token 不可以用")
            string_token.clear()
            string_ID.clear()
            get_token()
    else:
        print("没有 token，获取token")
        get_token()

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
    # 间隔3秒钟执行一次
    scheduler.add_job(tick_go_read_to_webBaoLiao, 'interval', seconds=10, max_instances=1)
    # 间隔3秒钟执行一次
    scheduler.add_job(tick_go_webDiQu_to_wx_and_webBaoLiao, 'interval', seconds=10, max_instances=1)
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
            if len(results_info) > 0:
                suobe_title,suobe_lists = format_into_a_dictionary_one(results_info[0])
                username,userpass,column =user(suobe_title)
                queue.put(read_suobe(username,userpass,column,suobe_lists))
                results_info.pop(0)
            if len(read_data_infos_title) > 0:
                queue.put(write_txt())
            if len(read_data_Webinfos_title) > 0:
                queue.put(read_suobe_BaoLiao())
                read_data_Webinfos_title.pop(0)
                read_data_Webinfos_video.pop(0)
                read_data_Webinfos_area.pop(0)
                read_data_Webinfos_time.pop(0)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print('Exit The Job!')