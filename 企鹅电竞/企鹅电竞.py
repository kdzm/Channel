from requestget import geturl
from requestget import posturl
import requests
from DPL频道列表模板 import lists
import re
import os
qq='https://egame.qq.com/gamelist'
headers={'referer':'https://egame.qq.com/gamelist/1','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
#class1={'一起看':'2000000110','主机游戏':'2000000140'}
class1={'一起看':'2000000110'}

def QQliveClass():
    r=geturl(qq,headers=headers)
    print(r)
    layoutid=re.findall(r'a href="/livelist\?layoutid=(.+?)"',r)
    titles=re.findall(r'target="_blank" title="(.+?)"',r)
    d=dict(zip(titles,layoutid))
    for x,y in d.items():
        print(x,y)
    return d
    #print(r)
#m=QQliveClass()
#del m['下载APP']
#print(m)
print('----------------------')
m1={'一起看':'2000000110'}
playurls=[]
for i,j in m1.items():
    print(i)
    #with open('企鹅电竞.txt', 'w', encoding="utf-8") as f:f.write('i\n')
    urls='https://egame.qq.com/livelist?layoutid='+j
    r=geturl(urls,headers=headers)
    #print(r)
    room_id=re.findall(r'<a href="/(\d*)"',r)
    room_name=re.findall(r'target="_blank" title="(.+?)"',r)
    del room_name[0]
    #print(len(room_id))
    #print(len(room_name))
    class_allroom=dict(zip(room_name,room_id))
    #del class_allroom['下载APP']
    for x,y in class_allroom.items():
        room_url='https://egame.qq.com/'+y
        res=geturl(room_url,headers=headers)
        playurl=re.findall(r'playUrl":"(.+?.flv)',res)
        if len(playurl)==0:
           playurl='http://3954.liveplay.myqcloud.com/live/3954_320942587.flv'
        else:
            playurl=playurl[0]
        playurls.append(playurl)
        print(x+'\t',playurl)
    print('----------------------')
with open('一起看.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('一起看.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in playurls:
    j=playurls.index(u)
    (x,y)=lists(room_name[j], u)
    with open('一起看.dpl', 'a+', encoding="utf-8") as f: f.write(str(j + 1) + x + "\n" + str(j + 1) + y + "\n" + str(j + 1) + '*played*0\n')
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\Channel\\企鹅电竞\\一起看.dpl')