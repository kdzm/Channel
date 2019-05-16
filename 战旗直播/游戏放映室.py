from requestget import geturl
import re
from DPL频道列表模板 import lists
from 战旗直播.base64a import zqbsurl
import os
#url='https://www.zhanqi.tv/games/Entertainment'
r_ids = []
r_nas = []
for i in range(1,3):
    url='https://www.zhanqi.tv/api/static/v2.1/game/live/45/30/'+str(i)+'.json'
    header={'Referer':'https://www.zhanqi.tv/','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    r=geturl(url,headers=header)
    r_id=re.findall(r'"url":"\\/(.+?)"',r)
    r_na = re.findall(r'"title":"(.+?)"', r)
    r_ids=r_ids+r_id
    r_nas=r_nas+r_na
#print(r_id)
'''
for i in range(0,21):
    del r_id[0]
'''
print(r_nas)
for i in r_nas:
    x=i.replace('\\\\','\\')
    r_nas[r_nas.index(i)]=x
    y=x.encode('utf-8').decode('unicode_escape')
    r_nas[r_nas.index(x)]=y
    #print(r_na[r_na.index(y)])
d=dict(zip(r_nas,r_ids))
#print(d)
playurls=[]
b=list(d.keys())

for x,y in d.items():
    urlr='https://www.zhanqi.tv/'+y
    r=geturl(urlr,headers=header)
    VideoLevels=re.findall(r'VideoLevels":"(.+?)"',r)
    a=zqbsurl(streamUrl=VideoLevels[0])
    playurls.append(a)
    print(x,a)
with open('游戏放映室.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('游戏放映室.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in playurls:
    j=playurls.index(u)
    (x,y)=lists(b[j], u)
    with open('游戏放映室.dpl', 'a+', encoding="utf-8") as f: f.write(str(j + 1) + x + "\n" + str(j + 1) + y + "\n" + str(j + 1) + '*played*0\n')
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\战旗直播\\游戏放映室.dpl')
'''
a='\u3016\u5e2b\u843d\u3017\u611f\u6069\u5c0f\u5b81\u7684\u652f\u6301\uff01\uff01\uff01'
b=str(a)
print(b)
'''