import requests
import string
import re

url="http://api.epg2.cibn.cc/v1/loopChannelList?epgId=1000"
headers={"user-agent":"Mozilla/5.0"}
r=requests.get(url,headers)
r.encoding='utf-8'
txt=r.text
#print(txt)
p1=r'"channelId":[0-9]{2,3},"channelName":".+?"'
p2=r'"m3u8":".+?"'
pattern1=re.compile(p1)
pattern2=re.compile(p2)
channelID2=pattern1.findall(txt)
channelurl3=pattern2.findall(txt)
print(channelurl3)
for x in channelID2:
#for i in range(len(channelurl3)):
    #print(x)
    #url=channelurl3[y].replace('"m3u8":"',"")
    y=channelID2.index(x)
    url=channelurl3[y].replace('"m3u8":"',"")
    url=url.replace('"',"")
    channel=x.replace('channelId":',"频道链接:http://cc.linkinme.com/cibn2/")
    channel=channel.replace("channelName","频道名称")
    print(channel,url)
    with open('cibn.txt','w',encoding="utf-8") as f:f.write(channel+url+"\n")
    #y=y+1
