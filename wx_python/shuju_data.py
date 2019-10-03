#coding=utf-8
import requests,queue
text = [1]
#队列
queue = queue.Queue()
#代码
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