import os
import string
from requestget import geturl
import re

list='http://api.dianshihome.com/api/kuyun/list'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3761.0 Safari/537.36 Edg/75.0.127.0'}
r=geturl(list,headers=headers)
p1=r'channelName":.+?",'
pattern1=re.compile(p1)
channelName=pattern1.findall(r)
p2=r'"channelId":.+?"}'
pattern2=re.compile(p2)
channelId=pattern2.findall(r)
channelNames=[]
channelIds=[]
for x in channelName:
    x=x.replace('channelName":"',"").replace('",',"")
    channelNames.append(x)
for y in channelId:
    y=y.replace('"channelId":"','').replace('"}','')
    channelIds.append(y)
a=dict(zip(channelNames,channelIds))
print(a)
name=a.keys()
print(name)
for x in name:
   url='http://gslb.dianshihome.com/gslb/streams?region=440000&isp=telecom&tm=&uuid=&sign=&ver=1.0.8&channel_id='+a[x]+'&extra=pointless'
   r=geturl(url,headers=headers)
   print(x,r)
