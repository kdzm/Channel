import re
import os
from requestget import geturl
from DPL频道列表模板 import lists
chl={"广州综合":'5c7f7072e4b01c17db18fbd5',"广州新闻":'5c7f6f73e4b01c17db18fbd3',"广州经济":'5c7f7097e4b01c17db18fbd7',"广州竞赛":'5c7f70b7e4b01c17db18fbd9',"广州影视":'5c7f70dce4b01c17db18fbdb',"广州少儿":'5c7f711de4b01c17db18fbdf',"广州生活":'5c7f70fee4b01c17db18fbdd',"广州花城":'5c7f7136e4b01c17db18fbe1'}

headers={'Referer':'https://tv.gztv.com/','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
playurls=[]
for x,y in chl.items():
    url='https://channel.gztv.com/channelf/viewapi/player/channelVideo?id='+y+'&commentFrontUrl=https://comment.gztv.com/commentf'
#url='https://channel.gztv.com/channelf/viewapi/player/channelVideo?id=5c7f7072e4b01c17db18fbd5&commentFrontUrl=https://comment.gztv.com/commentf'
    r=geturl(url,headers=headers)
    #print(r)
    n1=r.find("standardUrl='")+len("standardUrl='")
    n2=r.find("'",n1)
    playurl=r[n1:n2]
    print('http://cc.linkinme.com/guangzhou/'+y+x,playurl)
    playurls.append(playurl)
name=list(chl.keys())
with open('广州.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('广州.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in playurls:
    j=playurls.index(u)
    (x,y)=lists(name[j],u)
    with open('广州.dpl', 'a+', encoding="utf-8") as f: f.write(str(j + 1) + x + "\n" + str(j + 1) + y + "\n" + str(j + 1) + '*played*0\n')
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\广州电视台\\广州.dpl')
print(len('2d821d7e8dd09be48018c2bf1318448520ba7d86ed51905866dc6bc2c6071147'))
'''
http://cc.linkinme.com/guangzhou/5c7f7072e4b01c17db18fbd5    广州综合   
http://cc.linkinme.com/guangzhou/5c7f6f73e4b01c17db18fbd3    广州新闻
http://cc.linkinme.com/guangzhou/5c7f7097e4b01c17db18fbd7    广州经济
http://cc.linkinme.com/guangzhou/5c7f70b7e4b01c17db18fbd9    广州竞赛
http://cc.linkinme.com/guangzhou/5c7f70dce4b01c17db18fbdb    广州影视
http://cc.linkinme.com/guangzhou/5c7f711de4b01c17db18fbdf    广州少儿
http://cc.linkinme.com/guangzhou/5c7f70fee4b01c17db18fbdd   广州生活
'''