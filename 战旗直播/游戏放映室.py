from requestget import geturl
import re
from DPL频道列表模板 import lists
from 战旗直播.base64a import zqbsurl
import os
url='https://www.zhanqi.tv/games/Entertainment'
header={'Referer':'https://www.zhanqi.tv/','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
r=geturl(url,headers=header)
r_id=re.findall(r'href="/(.+?)"',r)
for i in range(0,21):
    del r_id[0]
r_na=re.findall(r'jpg" alt="(.+?")',r)
d=dict(zip(r_na,r_id))
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