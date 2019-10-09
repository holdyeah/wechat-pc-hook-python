#coding=utf-8
import requests,queue
from requests.packages import urllib3
from urllib.parse import urlencode
text = [1]
#微信安装路径
wechet_lujian = ''
#队列
queue = queue.Queue()
#从urllib3中消除警告
urllib3.disable_warnings()  
session = requests.Session()
#旧的piPei条目长度
pipei = '爆料'
old_PiPei_number = [0]
#piPei要写到web爆料的内容
piPei_info =[]
#旧的anti条目长度
anti = '艾特'
old_anti_number = [0]
#anti要写到web爆料的内容
anti_info =[]

#下列列表分别是标题,栏目.地区或者是记者名字,内容.(格式化数据后写入到下列列表中去在去写入web爆料中)
biaoti = []
lanmu = []
jizhe = []
diqu = []
neirou = []

#登录web爆料账号密码
webbiaoli_name = 'ds*****'
webbiaoli_password = '******'

#列表是读取到的内容列表
tonglian_infos_id =[]
tonglian_infos_title =[]
tonglian_infos_video =[]
tonglian_infos_area =[]
tonglian_infos_time =[]
#需求写入txt的列表
txt_id =[]
txt_title =[]
txt_video =[]
txt_area =[]
txt_time =[]
#登录的token
string_token = []
string_ID = []
string_cookie = []
#web地区登录账号密码
data_search= [
    {'account':'******','password':'******'},
    {'account':'******','password':'******'},
    {'account':'******','password':'******'},
    {'account':'******','password':'******'},
    {'account':'******','password':'******'},
    {'account':'******','password':'******'},
    {'account':'******','password':'******'},
    {'account':'******','password':'******'},
    {'account':'******','password':'******'},
    {'account':'******','password':'******'},
]
#获取登录token地址
url = 'http://pgc.******.cn/interfaces/login.do'
#登录的头文件
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/json; charset=UTF-8',
    'Referer': 'http://pgc.******.cn/tl/login.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
#获取内容地址
con_url='http://pgc.******.cn/interfaces/ContentSearch.do'
#获取内容的头
con_headers = {
    'Accept': '*/*',
    'Content-Type': 'application/json;charset=UTF-8',
    'Referer': 'http://pgc.******.cn/tl/static/contentManage/allContent.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
newsxml_url = 'http://pgc.******.cn/interfaces/buildNewsXML.do'