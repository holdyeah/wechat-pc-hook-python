import requests
import urllib

url = "http://127.0.0.1:2020/file"
test_str = "D:/2.mp4"
test22 = urllib.parse.quote(test_str)
payload='wxid=filehelper&msg='+ test22
print(payload)
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.post(url, headers=headers, data=payload)
print(response.text)
