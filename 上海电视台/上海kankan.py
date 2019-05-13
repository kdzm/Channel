import base64
import requests
from  requestget import geturl
from  requestget import posturl
import re
import string
import os
from DPL频道列表模板 import  lists
import random
chl={'东方卫视':'800081',"上海新闻":'800084',"外语频道":'800089',"都市频道":'800090',"艺术人文":'800453',"第一财经":'800092',"上海纪实":'800091'}
#x=str(random.randint(0,99999999)).zfill(8)
headers={'Referer':'http://live.kankanews.com/huikan/','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36','Host':'api.app.kankanews.com','Cookie':'UM_distinctid=16aa949e4df358-0ac377b00ee23e-7a1437-1fa400-16aa949e4e0379; _ga=GA1.2.1144532404.1557618353; acw_tc=b739529c15576183579242760e764b201e34d8bdf5ddfd364236c05649; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1'}
playurls=[]
for a,b in chl.items():
    x = str(random.randint(0, 99999999)).zfill(8)
    url='http://api.app.kankanews.com/kankan/v5/livePC/stream/live/?id='+b+'&'+x   #东方卫视
    r=geturl(url,headers=headers)
    r=base64.b64decode(r)
    r=str(r)
    n1=r.find('pcstream":"')+len('pcstream":"')
    n2=r.find('"',n1)
    playurl=r[n1:n2]
    playurl=playurl.replace("\\",'')
    playurls.append(playurl)
    print(a+str(x),playurl)
name=list(chl.keys())
with open('上海看看.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('上海看看.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in playurls:
    j=playurls.index(u)
    (x,y)=lists(name[j],u)
    with open('上海看看.dpl', 'a+', encoding="utf-8") as f: f.write(str(j + 1) + x + "\n" + str(j + 1) + y + "\n" + str(j + 1) + '*played*0\n')
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\上海电视台\\上海看看.dpl')