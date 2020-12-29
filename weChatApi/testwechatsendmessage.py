import requests
import urllib

url = "http://127.0.0.1:2020/send"
test = "[微笑]"+'\n'
test1 = "[微笑]"
test += test1
test22 = urllib.parse.quote(test)
#wxid_*****修改成自己要发送的wxid或者群
payload='wxid=wxid_*****&msg='+ test22
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.post(url, headers=headers, data=payload)
print(response.text)
