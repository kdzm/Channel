from requestget import  geturl
from DPL频道列表模板 import lists
import requests
import os
import re
channels={'河南卫视':'135','河南新闻':'140','河南国际':'144','河南都市':'136','河南公共':'142','河南民生':'137','河南政法':'138','河南电视剧':'139','河南新农村':'143','晴彩中原':'145','河南航空港':'146','武术世界':'147','梨园频道':'148','文物宝库':'149'}
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Referer': 'http://www.hntv.tv/soms4/web/jwzt/player/flashplayer/program_live_player_flash.jsp?function=GetLiveProgramInfo&channelId=135'}
playurls=[]

for x,y in channels.items():
    url='http://www.hntv.tv/soms4/web/jwzt/player/live_ipad_player.jsp?channelId='+y
    #http://www.hntv.tv/soms4/web/jwzt/player/live_ipad_player.jsp?channelId=
    r=geturl(url,headers=headers)
    n1=r.find('src="')+len('src="')
    n2=r.find('"',n1)
    playurl=r[n1:n2]
    #print(r)
    #res = requests.get(url,allow_redirects=False)
    #la = res.headers['Location']
    #res.encoding='utf-8'
    #r.encoding='GB2312'
    #r=res.text
    #print(r)
    #playurl.append(la)
    playurls.append(playurl)
    print(x,playurl)
b=list(channels.keys())
with open('hntv.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('hntv.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in playurls:
    j=playurls.index(u)
    (x,y)=lists(b[j], u)
    with open('hntv.dpl', 'a+', encoding="utf-8") as f: f.write(
        str(j + 1) + x + "\n" + str(j + 1) + y + "\n" + str(j + 1) + '*played*0\n')
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\河南电视台\\hntv.dpl')