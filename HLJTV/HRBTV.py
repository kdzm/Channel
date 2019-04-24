import re
from requestget import geturl
import requests
import io
import string
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url1='http://liveapp.cutv.com/crossdomain/timeshiftinglive/getTSLAllChannelList/first/sztv'
t=geturl(url1,headers)
print(t)
p1=r'flag":".+?","channellist"'
pattern=re.compile(p1)
name=pattern.findall(t)
print(name)
names=[]
zs=[]
ys=[]
for x in name:
    x=x.replace('flag":"','').replace(',"channellist"','').replace('","name":"','')
    n=x.find("\\")
    y=x[0:n]
    #print(y)
    ys.append(y)
    z=x[n:-1]
    #print(z)
    zs.append(z)
    #z1=z.decode('unicode-escape')
    names.append(x)
#print(names)
ys.pop(-3)
zs.pop(-3)
print(ys)
print(zs)
print(len(zs))
ls=[]
for i in zs:
    i=i.encode('utf-8').decode('unicode_escape')
    ls.append(i)
print(ls)
p2=r'"channellist":.+?{"flag"'
pattern2=re.compile(p2)
list=pattern2.findall(t)
print(list)
print(len(list))
#for m in list:

