import requests
url="http://cc.linkinme.com/hljtv5/9"
headers={"Referer":"http://www.hljtv.com/live/folder424/","User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
r=requests.get(url,headers)
r.encoding='utf-8'
r=r.text
print(r)