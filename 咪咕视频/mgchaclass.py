from requestget import geturl
import re
import string
from MD5 import get_token
import time
def mgreurl():
    name = []
    id = []
    xurls = []
    url1='http://live.miguvideo.com/live/v2/tv-data/70002091'
    headers={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12F70 MicroMessenger/6.2.3 NetType/WIFI Language/zh_CN'}
    r1=geturl(url1,headers=headers)
#print(r1)
    cha_classs=re.findall(r'name":".+?vomsID',r1)
    class_id=re.findall(r'"vomsID":".+?"',r1)
#print(cha_classs)
    #mgch=dict()
    for x in cha_classs:
        cha_classs[cha_classs.index(x)]=x.replace('name":"','').replace('","vomsID','')
#print(cha_classs)
    for y in class_id:
        class_id[class_id.index(y)]=y.replace('"vomsID":"','').replace('"','')
#print(class_id)
    cla=dict(zip(cha_classs,class_id))
    for x,y in cla.items():
    #print(x,y)
        #print(x)
        url='http://live.miguvideo.com/live/v2/tv-data/'+y
        r=geturl(url,headers=headers)
        channels=re.findall(r'name":".+?"',r)
        for a  in range(0,len(cla)):
            del channels[0]
    #print(channels)
        for b in channels:
            channels[channels.index(b)]=b.replace('name":"',"").replace('"','')
    #print(channels)
        channels_id=re.findall(r'pID":".+?"',r)
        for c in channels_id:
            channels_id[channels_id.index(c)]=c.replace('pID":"','').replace('"','')
    #print(channels_id)
        channels_=dict(zip(channels,channels_id))
    #mgch=mgch+channels_
        for i,j in channels_.items():
        #print(x,y)
            id.append(j)
            name.append(i)
            t=str(int(time.time()))
            clientId=get_token(message=t).upper()
            xurl='http://yk.miguvideo.com/playurl/v1/play/playurlh5?contId='+j+'&rateType=2&clientId='+clientId
            #print(i,xurl)
            xurls.append(xurl)
            #return
        #print('**************************************')
    ch=dict(zip(name,xurls))
    #print(ch)
    return ch


#print(mgch)