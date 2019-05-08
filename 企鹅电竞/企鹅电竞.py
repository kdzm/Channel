from requestget import geturl
from requestget import posturl
import requests
import re
listurl='https://egame.qq.com/livelist?layoutid=2000000110'
headers={'referer':'https://egame.qq.com/gamelist/1','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
r=geturl(listurl,headers=headers)
#print(r)
p1=r'data-v-93e92c10><a href="/.+?"'
p2=r'target="_blank" title=".+?"'
pattern1=re.compile(p1)
pattern2=re.compile(p2)
a=[]
b=[]
namers=pattern1.findall(r)
ids=pattern2.findall(r)
for x in namers:
    x=x.replace('data-v-93e92c10><a href="/','').replace('"','')
    a.append(x)
for y in ids:
    y=y.replace('target="_blank" title="','').replace('"','')
    b.append(y)
d=dict(zip(a,b))
for x,y in d.items():
    print(x,y)