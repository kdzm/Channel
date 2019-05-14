from requestget import geturl
import re
import string
names=[]
adds=[]
for i in range(1,2):
    url='http://chlist.sopplus.tv/v1/channels'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    r=geturl(url,headers)
    name=re.findall(r'"name": ".+?"',r)
    add=re.findall(r'"address": ".+?"',r)
for x in name:
    name[name.index(x)]=x.replace('"name": "','').replace('"','')
        #names.append(a)
for y in add:
    add[add.index(y)] = y.replace('"address": "', '').replace('"', '')
        #adds.append(b)
#print(name)
#print(add)
d=dict(zip(name,add))
for x,y in d.items():
    print(x+'\b'+y)
    with open('tvbus.txt', 'a+', encoding="utf-8") as f: f.write(x+'\b'+y+'\n')
