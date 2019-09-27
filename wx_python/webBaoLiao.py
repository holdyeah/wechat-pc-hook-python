#coding=utf-8
import time,shutil,re

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
    findanti =r"(?<=@小蜗牛 )\d*"
    pattern_word = re.compile(findword)
    pattern_anti = re.compile(findanti)
    results_word = pattern_word.findall(strlist1)
    results_anti = pattern_anti.findall(strlist1)
    return results_word,len(results_word),results_anti,len(results_anti)

#检查新的扫描内容，跟旧的内容是否一致，是则不变，否则增加新内容到results_info
def run_results_number(results,old_results_number,news_results_number,results_info):
    print("当前扫描文件内一共有: " +str(news_results_number) + " 条内容")
    if news_results_number-old_results_number[0] ==0:
        #print("无新增内容")
        old_results_number[0] = news_results_number
    else:
        print("扫描到有新内容,添加到列表成功")
        increase_results_number =[0]
        increase_results_number[0] = news_results_number-old_results_number[0]
        for index_number in range(increase_results_number[0]):
            info = results[old_results_number[0]+index_number]
            results_info.append(info) 
        old_results_number[0] = news_results_number

def tick_go_read_to_webBaoLiao():
    print('获取read.txt中相关信息写入到web爆料!')