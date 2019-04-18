import re
import string
from requestget import geturl
import os
from DPL频道列表模板 import lists
lista={"石家庄新闻":"2","石家庄娱乐":"3","石家庄生活":"4","石家庄都市":"5",}
with open('石家庄.dpl', 'w', encoding="utf-8") as f: f.write("")
with open('石家庄.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0'+'\n')
urs=[]
for x,y in lista.items():
    url='http://mobile.sjzntv.cn/app/channel_detail.php?appid=8&appkey=BJaFDrsqqZQelNRXE6EhUXmlfzhq5Rox&device_token=6b07de2166a86e9dbbfb570268574467&_member_id=&version=2.0&app_version=2.0&app_version=2.0&package_name=com.hoge.android.app.wxsjz&system_version=4.4.4&phone_models=VAY_32MOS&ad_group=mobile&channel_id='+y
    headeers={"user-agent":"Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; VAY_32MOS Build/KOT49H) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"}
    r=geturl(url,headers=headeers)
    #print(x,r)
    n1=r.find('"url":"http')+len('"url":"')
    n2=r.find('","name"',n1)
    url1=r[n1:n2]
    url2=url1.replace("\\","")
    urs.append(url2)
    print(x,url2)
    with open('石家庄.html', 'a', encoding="utf-8") as f: f.write(x+url2)
for u in urs:
    name=list(lista.keys())
    j = urs.index(u)
    (m,n) = lists(name[j], u)
    with open('石家庄.dpl', 'a+', encoding="utf-8") as f: f.write(str(j + 1) + m + "\n" + str(j + 1) + n + "\n" + str(j + 1) + '*played*0\n')
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\地方台\\石家庄.dpl')


