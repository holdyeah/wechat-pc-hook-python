#coding=utf-8
import time,shutil,re,requests
import shuju_data
from bs4 import BeautifulSoup
#复制文本到命名为2000-01-01.txt格式 copy_filename路径下
def copy_wx_file_to_cpyefilename(wx_filename,copy_filename):
    newstime = time.strftime('%Y-%m-%d',time.localtime())
    shutil.copy(wx_filename,copy_filename+newstime+'.txt')

#扫描txt内容匹配开头是#结尾是&的内容，返回指定内容和条数.@小蜗牛 1111 内容和条数
def screening_txtData(filename):
    TXTtemp = open(filename,encoding='utf-8')
    txtbuffer=TXTtemp.read()
    strlist1=txtbuffer.replace("\n"," ")
    findword =u"(#.*?&)"
    findanti =r"(?<=@小蜗牛)\d*"
    pattern_word = re.compile(findword)
    pattern_anti = re.compile(findanti)
    results_word = pattern_word.findall(strlist1)
    results_anti = pattern_anti.findall(strlist1)
    return results_word,len(results_word),results_anti,len(results_anti)

#检查新的扫描内容，跟旧的内容是否一致，是则不变，否则增加新内容到results_info(名字,数据,旧的数据长度,新的数据长度,加到那个列表)
def run_results_number(name,results,old_results_number,news_results_number,results_info):
    #print("当前扫描文件内匹配到共有: " +str(news_results_number) + " 条内容")
    if news_results_number-old_results_number[0] ==0:
        #print("无新增内容")
        old_results_number[0] = news_results_number
    else:
        print("匹配到"+ name + str(news_results_number-old_results_number[0]) +"条新内容,添加到列表成功")
        increase_results_number =[0]
        increase_results_number[0] = news_results_number-old_results_number[0]
        for index_number in range(increase_results_number[0]):
            info = results[old_results_number[0]+index_number]
            results_info.append(info) 
        old_results_number[0] = news_results_number

#格式化内容返回标题和内容
def format_into_a_dictionary_one(into):
    into_data = into
    size_up_number = []
    newstime = time.strftime('%Y%m%d',time.localtime())
    wu  = into_data.find('#')
    wu_time  = into_data.find(newstime)
    fen_hao  = into_data.find(':')
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
    lanmu = into_data[size_up_number[20]+8:size_up_number[21]]
    number = -1
    index_number = size_up_number.index(number)
    for index in range(index_number):
        str0 = into_data[size_up_number[index]:size_up_number[index+1]]
        info_size_up_number =[]
        dun_hao     = str0.find('、')
        fu_place    = str0.find('地点')
        fu_reporter = str0.find('记者')
        fu_content  = str0.find('内容')
        fu_test  = str0.find('飝靁')
        info_size_up_number.append(dun_hao)
        info_size_up_number.append(fu_place)
        info_size_up_number.append(fu_reporter)
        info_size_up_number.append(fu_content)
        info_size_up_number.append(fu_test)
        index_size_number = info_size_up_number.index(number)
        if index_size_number == 1:
            title_info = (str0[dun_hao+1:])
            #print(lanmu,title_info)
            shuju_data.biaoti.append(title_info)
            shuju_data.lanmu.append(lanmu)
            shuju_data.jizhe.append('0')
            shuju_data.diqu.append('0')
            shuju_data.neirou.append(title_info)
        elif index_size_number == 2:
            title_info = (str0[dun_hao+1:fu_place])
            place = (str0[fu_place+3:])
            #print(lanmu,title_info,place)
            shuju_data.biaoti.append(title_info)
            shuju_data.lanmu.append(lanmu)
            shuju_data.jizhe.append('0')
            shuju_data.diqu.append(place)
            shuju_data.neirou.append(title_info)
        elif index_size_number == 3:
            title_info = (str0[dun_hao+1:fu_place])
            place = (str0[fu_place+3:fu_reporter])
            reporter = (str0[fu_reporter+3:])
            #print(lanmu,title_info,place,reporter)
            shuju_data.biaoti.append(title_info)
            shuju_data.lanmu.append(lanmu)
            shuju_data.jizhe.append(reporter)
            shuju_data.diqu.append(place)
            shuju_data.neirou.append(title_info)
        elif index_size_number == 4:
            title_info = (str0[dun_hao+1:fu_place])
            place = (str0[fu_place+3:fu_reporter])
            reporter = (str0[fu_reporter+3:fu_content])
            content = (str0[fu_content+3:])
            #print(lanmu,title_info,place,reporter,content)
            shuju_data.biaoti.append(title_info)
            shuju_data.lanmu.append(lanmu)
            shuju_data.jizhe.append(reporter)
            shuju_data.diqu.append(place)
            shuju_data.neirou.append(content)

#检查web是否正常
def check_network():
    res_network = shuju_data.session.get("https://cas********",verify=False)
    return res_network.status_code

#检查网络，正常就把内容写入到web爆料中
def read_suobe():
    time.sleep(2)
    while True:
        driver_status_code = check_network()
        if driver_status_code != 200:
            print("网络错误")
            time.sleep(150)
            continue
        elif driver_status_code == 200:
            print("网络正常")
            to_webBaoLiao()
            print("=======")
            break
    print("关闭")

#biaoti,lanmu,neirou,jizhe,diqu,shoujihao
def to_webBaoLiao():
    print('写入到web爆料!')
    time.sleep(1)
    while True:
        session = requests.Session()
        time.sleep(2)
        login_cookies = ''
        login_lt=''
        login_strTemp=''
        login_e1s2=''
        respon_get = session.get("https://cas********",verify=False)
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
            'Referer': 'https://cas.*****',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        }
        login_data='username='+shuju_data.webbiaoli_name+'&strTemp='+login_strTemp+'&password='+shuju_data.webbiaoli_password+'&lt='+login_lt+'&execution='+login_e1s2+'&_eventId=submit&submit=%E7%AB%8B%E5%8D%B3%E7%99%BB%E5%BD%95'
        login_url = 'https://cas.*****.cn'
        login_response=session.post(login_url,headers=login_headers,data=login_data,verify=False)
        print(login_response.status_code)
        if login_response.status_code != 200:
            print("登录失败")
            time.sleep(10)
            continue
        elif login_response.status_code == 200:
            print("登录成功")
            time.sleep(2)
            url_ecc='http://ecc.*****.cnloginCas;jsessionid='+session.cookies['JSESSIONID']+'?key=menu_bl'
            ecc_get = session.get(url_ecc,verify=False)
            ecc_token ='siteCode=S1; token='+ecc_get.url[69:]
            ecc_headers ={
                'Accept':'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'cas.*****.cn',
                'Connection': 'keep-alive',
                'Origin': 'http://cas.*****.cn',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                'Content-Type': 'application/json;charset=UTF-8',
                'Referer': 'http://cas.*****.cntpp/',
                "Referrer Policy":"no-referrer-when-downgrade",
                'Cookie': ecc_token,
            }
            print(len(shuju_data.biaoti))
            info_size_up_number = len(shuju_data.biaoti)
            for index in range(info_size_up_number):
                print(index)
                columnCode = ""
                columnname = ""
                if shuju_data.lanmu[0] == "cas.*****.cn":
                    columnCode = "cas.*****.cn"
                    columnname = "cas.*****.cn"
                elif shuju_data.lanmu[0] == "cas.*****.cn":
                    columnCode = "cas.*****.cn"
                    columnname = "cas.*****.cn"
                elif shuju_data.lanmu[0] == "cas.*****.cn":
                    columnCode = "cas.*****.cn"
                    columnname = "cas.*****.cn"
                elif shuju_data.lanmu[0] == "cas.*****.cn":
                    columnCode = "cas.*****.cn"
                    columnname = "cas.*****.cn"
                else:
                    columnCode = "cas.*****.cn"
                    columnname = "cas.*****.cn"
                description = shuju_data.neirou[0]
                title = shuju_data.biaoti[0]
                createUserName = "cas.*****.cn"
                siteName  = "cas.*****.cn"
                data_ecc ='''{\"strategy\":{\"send\":true,\"task\":false},\"columnCode\":\"'''+columnCode+'''\",\"description\":\"<p>'''+description+'''</p>\",\"source\":\"4\",\"category\":\"1\",\"title\":\"'''+title+'''\",\"phone\":\"test\",\"clueCreateTime\":null,\"columnname\":\"'''+columnname +'''\",\"createUserCode\":\"6E76\",\"createUserName\":\"'''+createUserName+'''\",\"siteCode\":\"S1\",\"siteName\":\"'''+ siteName +'''\"}'''
                #print(data_ecc)
                url_ecc_post='http://cas.*****.cn/tpp/rest/content/clue/add'
                response_ecc=session.post(url_ecc_post,data=data_ecc.encode('utf-8'),headers=ecc_headers,verify=False)
                #print(response_ecc.json())
                uuid = response_ecc.json()['data'][0]['uuid']
                uuid_url = 'http://cas.*****.cn/tpp/rest/content/clue/updateStatus?uuid='+uuid
                headers_uuid ={
                    'Accept':'application/json, text/plain, */*',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Host': 'cas.*****.cn',
                    'Connection': 'keep-alive',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                    'Content-Type': 'application/json;charset=UTF-8',
                    'Referer': 'http://cas.*****.cn/tpp/',
                    'Cookie': ecc_token,
                }
                response_uuid=session.get(uuid_url,headers=headers_uuid,verify=False)
                print(response_uuid.json())
                #删除列表第一个
                shuju_data.biaoti.pop(0)
                shuju_data.lanmu.pop(0)
                shuju_data.jizhe.pop(0)
                shuju_data.diqu.pop(0)
                shuju_data.neirou.pop(0)
                