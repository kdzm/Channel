import os
import string
from requestget import geturl
import requests
import re

list='http://bdapp.lntv.cn:8242/api/lntv/living/tv'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3761.0 Safari/537.36 Edg/75.0.127.0','Referer': 'http://bdapp.lntv.cn/e/extend/lntv/gt.php','Host': 'bdapp.lntv.cn'
}
headers1={'User-Agent':'Dalvik/1.6.0 (Linux; U; Android 4.4.2; VAM_H8 Build/KOT49H)','Referer': 'http://bdapp.lntv.cn/e/extend/lntv/gt.php'}
data={"appkey" : "GY3h7uP9RU8gAFU2Nb33a6Tk4e5GqwcawFzf6JLqmd4nrYqH","key" :'A900590836FC536B1B6AA82F8876E23922CDCB574C22F293E756D4BF2D15C292E6E0C60A5B4EB862BE2B57F0BC140818BF9C867AD6F019CDE6CFC53BF5A0A958A988C2F41D183EBCA35EC11923285892D04C6D4166CA8BD0C1949224D251201B197099C9331E9BA5B155C2F41D5'}
r=geturl(list,headers=headers)
print(r)
p1=r'http:.+?","'
pattern1=re.compile(p1)
http=pattern1.findall(r)
p2=r':"update","name":".+?"'
pattern2=re.compile(p2)
name=pattern2.findall(r)
list=[]
name2=[]
for x in http:
    x=x.replace('\\','').replace('","','')
    #print(x)
    list.append(x)
list2=list[0:len(list)-1:2]
for y in name:
    y=y.replace(':"update","name":"','').replace('"','')
    name2.append(y)
    #print(y)
d=dict(zip(name2,list2))
for x,y in d.items():
    print(x,y)

#http://bdtvlive.lntv.cn/bdapp/lntv.m3u8?auth_key=1555321968-5cb454709150b-0-8d25c794d0dcc1cb0c13adabab990181
#http://bdtvlive.lntv.cn/bdapp/lnds.m3u8?auth_key=1555321968-5cb4547091550-0-9131ad0bb075645ea2c3120645c3c366