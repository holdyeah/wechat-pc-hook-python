#coding=utf-8
import shuju_data
import random,json

#判断write.txt是否有内容，无则写入一条内容，有则不写入
def write_txt():
    #微信read.txt目录
    wx_filename = shuju_data.wechet_lujian+'\\write.txt'
    #print("判断txt写入")
    txt_open = open(wx_filename,'r')
    txt = txt_open.read()
    txt_open.close()
    if(txt == ''):
        print("写入txt")
        data = open(wx_filename,'w+')
        txt_data1 = shuju_data.txt_title[0]
        #判断有没有视频
        txt_data2 = ""
        if shuju_data.txt_video[0] == '':
            txt_data2 += " 还没有发视频 "
        else:
            txt_data2 += " 有视频 "
        txt_data3 = shuju_data.txt_area[0]
        txt_data4 = shuju_data.txt_time[0]
        txt_data5 = "编号：" + str(shuju_data.txt_id[0])
        txt_data1 += txt_data2
        txt_data1 += txt_data3
        txt_data1 += txt_data4
        txt_data1 += txt_data5
        data.write(txt_data1)
        data.close()
        shuju_data.txt_id.pop(0)
        shuju_data.txt_title.pop(0)
        shuju_data.txt_video.pop(0)
        shuju_data.txt_area.pop(0)
        shuju_data.txt_time.pop(0)
    else:
        print("扫描到txt中有内容，不写入，等待")

#艾特的数据发送小飞机
def anti():
    newsxml_headers = {
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Host': 'pgc.******.cn',
        'Origin': 'http://pgc.******.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Referer': 'http://pgc.******.cn/tl/static/contentManage/allContent.html',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': shuju_data.string_cookie[0],
    }
    newsxml_search= {
        "userId":shuju_data.string_ID[0],
        "token":shuju_data.string_token[0],
        "contentId":shuju_data.anti_info[0]
    }
    shuju_data.session.post(shuju_data.newsxml_url,headers=newsxml_headers,data=json.dumps(newsxml_search),timeout = 20)
    #print((response2))

#随机获取data_search其中一个数登录获取token,用户ID
def get_token():
    data_nmber = len(shuju_data.data_search)-1
    ran = random.randint(0,data_nmber)
    response=shuju_data.session.post(shuju_data.url,headers=shuju_data.headers,data=json.dumps(shuju_data.data_search[ran]))
    JSESSIONID = shuju_data.session.cookies['JSESSIONID']
    cookie = 'JSESSIONID='+JSESSIONID
    shuju_data.string_cookie.append(cookie)
    shuju_data.string_token.append(response.json()['token'])
    shuju_data.string_ID.append(response.json()['ID'])

#post获取信息，返回内容的长度和内容,获取 infos
def get_infos():
    con_search= {
        "userId":shuju_data.string_ID[0],
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
        "token": shuju_data.string_token[0],
    }
    infos_response=shuju_data.session.post(shuju_data.con_url,headers=shuju_data.con_headers,data=json.dumps(con_search),timeout = 20)
    return len(infos_response.json()),infos_response

#判断内容是否有新
def decide_infos(infos_response):
    #infos_response的长度
    index_data = len(infos_response.json()["pdList"])
    #下列列表内容是 编号id 标题 视频 地区 时间 
    info_id = []
    info_title =[]
    info_video =[]
    info_area =[]
    info_time =[]
    data_index = 0
    for index in range(index_data):
        info_id.append(infos_response.json()["pdList"][index]["ID"])
        info_title.append(infos_response.json()["pdList"][index]["TITLE"])
        info_video.append(infos_response.json()["pdList"][index]["ATTACHMENTTYPE"])
        info_area.append(infos_response.json()["pdList"][index]["USERNAME"])
        info_time.append(infos_response.json()["pdList"][index]["CREATETIME"])
    #判断tonglian_infos_id里面是否有值,有值判断是否有新的视频或者新的条目,无值则把内容加入到以下列表中去
    if len(shuju_data.tonglian_infos_id):
        #tonglian_infos_id 里面有值
        #判断新的列表跟旧列表第一条是一致的
        if(shuju_data.tonglian_infos_id[0] == info_id[0]):
            #print("新的列表跟旧列表第一条是一致")
            #判断新的列表跟旧列表的ATTACHMENTTYPE有没有变化
            for info_index in range(index_data):
                if info_video[info_index] != shuju_data.tonglian_infos_video[info_index]:
                    shuju_data.txt_id.append(info_id[info_index])
                    shuju_data.txt_title.append(info_title[info_index])
                    shuju_data.txt_video.append(info_video[info_index])
                    shuju_data.txt_area.append(info_area[info_index])
                    shuju_data.txt_time.append(info_time[info_index])
                    #添加数据到爆料列表中去
                    shuju_data.biaoti.append(info_title[info_index])
                    shuju_data.lanmu.append('0')
                    shuju_data.jizhe.append('0')
                    shuju_data.diqu.append(info_area[info_index])
                    shuju_data.neirou.append(info_title[info_index])

            #循环完毕后做一个清除tonglian_infos_**  list clear()
            shuju_data.tonglian_infos_id.clear()
            shuju_data.tonglian_infos_title.clear()
            shuju_data.tonglian_infos_video.clear()
            shuju_data.tonglian_infos_area.clear()
            shuju_data.tonglian_infos_time.clear()  
            #附加新的列表值到tonglian_infos_**  list
            for index in range(index_data):
                shuju_data.tonglian_infos_id.append(infos_response.json()["pdList"][index]["ID"])
                shuju_data.tonglian_infos_title.append(infos_response.json()["pdList"][index]["TITLE"])
                shuju_data.tonglian_infos_video.append(infos_response.json()["pdList"][index]["ATTACHMENTTYPE"])
                shuju_data.tonglian_infos_area.append(infos_response.json()["pdList"][index]["USERNAME"])
                shuju_data.tonglian_infos_time.append(infos_response.json()["pdList"][index]["CREATETIME"])         
        else:
            #print("新的列表跟旧列表第一条不一致")
            #判断有几条不一样的
            for new_index in range(len(info_id)):
                if(shuju_data.tonglian_infos_id[0] == info_id[new_index]):
                    data_index += new_index
            if(data_index != 0):
                #print("写入到txt web列表")
                for txt_index in range(data_index):
                    shuju_data.txt_id.append(info_id[txt_index])
                    shuju_data.txt_title.append(info_title[txt_index])
                    shuju_data.txt_video.append(info_video[txt_index])
                    shuju_data.txt_area.append(info_area[txt_index])
                    shuju_data.txt_time.append(info_time[txt_index])
                    #添加数据到爆料列表中去
                    if info_video[txt_index] != '0':
                        shuju_data.biaoti.append(info_title[txt_index])
                        shuju_data.lanmu.append('0')
                        shuju_data.jizhe.append('0')
                        shuju_data.diqu.append(info_area[txt_index])
                        shuju_data.neirou.append(info_title[txt_index])
                #新列表中的后面跟旧的列表一致的ATTACHMENTTYPE有没有变化
                for old_index in range(len(info_id) - data_index):
                    if info_video[data_index + old_index] != shuju_data.tonglian_infos_video[old_index]:
                        shuju_data.txt_id.append(info_id[data_index + old_index])
                        shuju_data.txt_title.append(info_title[data_index + old_index])
                        shuju_data.txt_video.append(info_video[data_index + old_index])
                        shuju_data.txt_area.append(info_area[data_index + old_index])
                        shuju_data.txt_time.append(info_time[data_index + old_index])
                        #添加数据到爆料列表中去
                        shuju_data.biaoti.append(info_title[data_index + old_index])
                        shuju_data.lanmu.append('0')
                        shuju_data.jizhe.append('0')
                        shuju_data.diqu.append(info_area[data_index + old_index])
                        shuju_data.neirou.append(info_title[data_index + old_index])
            #循环完毕后做一个清除tonglian_infos_**  list clear()
            shuju_data.tonglian_infos_id.clear()
            shuju_data.tonglian_infos_title.clear()
            shuju_data.tonglian_infos_video.clear()
            shuju_data.tonglian_infos_area.clear()
            shuju_data.tonglian_infos_time.clear()  
            #附加新的列表值到tonglian_infos_**  list
            for index in range(index_data):
                shuju_data.tonglian_infos_id.append(infos_response.json()["pdList"][index]["ID"])
                shuju_data.tonglian_infos_title.append(infos_response.json()["pdList"][index]["TITLE"])
                shuju_data.tonglian_infos_video.append(infos_response.json()["pdList"][index]["ATTACHMENTTYPE"])
                shuju_data.tonglian_infos_area.append(infos_response.json()["pdList"][index]["USERNAME"])
                shuju_data.tonglian_infos_time.append(infos_response.json()["pdList"][index]["CREATETIME"])                                

    else:
        #tonglian_infos_id 里面无值
        for index in range(index_data):
            shuju_data.tonglian_infos_id.append(infos_response.json()["pdList"][index]["ID"])
            shuju_data.tonglian_infos_title.append(infos_response.json()["pdList"][index]["TITLE"])
            shuju_data.tonglian_infos_video.append(infos_response.json()["pdList"][index]["ATTACHMENTTYPE"])
            shuju_data.tonglian_infos_area.append(infos_response.json()["pdList"][index]["USERNAME"])
            shuju_data.tonglian_infos_time.append(infos_response.json()["pdList"][index]["CREATETIME"])


#获取web地区新条目发送到微信和写入到web爆料
def panduan_webqidu():
    if len(shuju_data.string_token):
        #有token
        status_code,infos_response = get_infos()
        if status_code == 3:
            #token可以用
            shuju_data.queue.put(decide_infos(infos_response))
        else:
            #token不可以用,清空string_token,string_ID
            shuju_data.string_token.clear()
            shuju_data.string_ID.clear()
            shuju_data.string_cookie.clear()
            get_token()
    else:
        #没有token,获取token
        get_token()