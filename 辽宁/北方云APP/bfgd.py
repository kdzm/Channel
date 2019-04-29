from MD5 import get_token
import requests
from requestget import  geturl
from requestget import posturl
#http://slave.bfgd.com.cn:13160/account/get_access_token
import string
import re
import random
import json
headers1={'User-Agent':'Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G900F Build/KOT49H)'}
def firstdevc(Deviceno='69DCCBEC6DFECD4A8EE17509EE7D7D77f'):
    url2='http://slave.bfgd.com.cn:13160/account/get_access_token'
    datas=json.dumps({"deviceType":"yuj","deviceno":Deviceno,"role":"guest"})
    r2=posturl(url2,data=datas,headers=headers1)
    #print(r2)
    n1=r2.find('"accessToken":"')+len('"accessToken":"')
    n2=r2.find('","',n1)
    accessToken=r2[n1:n2]
    return accessToken

def access_token(devc1=firstdevc()):
    #devc1=firstdevc()
    get_accesstoken='http://access.bfgd.com.cn:12690/account/login?isforce=1&accesstoken='+devc1+'&accounttype=2&deviceno='+'69DCCBEC6DFECD4A8EE17509EE7D7D77f&pwd=96e79218965eb72c92a549dd5a330112&devicetype=3&account=40169031313'
    r3=geturl(get_accesstoken,headers=headers1)
    #print(r3)
    n1=r3.find('"access_token" : "')+len('"access_token" : "')
    n2=r3.find('",',n1)
    access_tokens=r3[n1:n2]
    n3=r3.find('"device_id" : ')+len('"device_id" : ')
    n4=r3.find(',',n3)
    verifycode =r3[n3:n4]
    return (access_tokens,verifycode)

(a,c)=access_token()
listtype={'1775': "高清频道",'2114': "标清频道",'3256': "本地频道",'3520':"国际频道"}
channel_ids = []
channel_names = []
for l in listtype:
    idurl='http://slave.bfgd.com.cn:13160/homed/program/get_list?musicsize=246x138&label='+l+'&accesstoken='+a+'&pagenum=78&vodsize=246x138&chnlsize=90x90%7C246x138&pageidx=1&livesize=246x138&hdsize=246x138&appsize=246x138&sdsize=246x138'
    r1=geturl(idurl,headers=headers1)
    #print(r1)
#print(r1)
    p1=r'{"id":4200000[0-9]{3}'
    p2=r':1,"name":".+?"'
    pattern1=re.compile(p1)
    pattern2=re.compile(p2)
    channel_id=pattern1.findall(r1)
    channel_name=pattern2.findall(r1)
    for id in channel_id:
        id=id.replace('{"id":','')
        channel_ids.append(id)
    for name in channel_name:
        name=name.replace(':1,"name":"','').replace('"','')
        channel_names.append(name)
    channels=dict(zip(channel_names,channel_ids))
print(channels)
'''for x,y in channels.items():
    print(x,y)
#得到频道名称和频道id
'''

n=random.randint(0,len(channel_name)-1)
#print(n)
deviceno=get_token('4200000081'+'yzw123')
#print(deviceno)
Deviceno1=deviceno.upper()
#print(Deviceno1)
#产生设备号
dec=firstdevc(Deviceno=Deviceno1)#得到accessToken
(a_c,verifycode)=access_token(devc1=dec)#得到access_token
#print(a_c,verifycode)
'''
for x,y in channels.items():
    url3='http://slave.bfgd.com.cn:13160/media/channel/get_info?accesstoken='+a_c+'&chnlid='+channel_ids[0]+'&verifycode='+verifycode
    r=geturl(url3,headers=headers1)
    #print(r)
    n1=r.find('"play_token":"')+len('"play_token":"')
    n2=r.find('","',n1)
    playtoken=r[n1:n2]
    playurl='http://httpdvb.slave.bfgd.com.cn/playurl?playtype=live&protocol=http&accesstoken='+a_c+'&programid='+y+'&playtoken='+playtoken+'&verifycode='+verifycode
    print(x,playurl)'''
    #http://httpdvb.slave.bfgd.com.cn/playurl?playtype=live&protocol=http&accesstoken=R5CC27A56U3089D04BKB2D9E4F4I1993903DP8M316BC69WE276CCABF61&programid=4200000081&playtoken=31614VJHSLMFKWW10&rate=sd&verifycode=3000624372
#get_accesstoken='http://access.bfgd.com.cn:12690/account/login?isforce=1&accesstoken=GD4C27A39V11307D1T1A205C5FJD43D0EABM7F8DDE8CI1993903D&accounttype=2&deviceno=4EA08CBF558007607004D93699A29423&pwd=96e79218965eb72c92a549dd5a330112&devicetype=3&account=40169031313'