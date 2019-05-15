from requestget import geturl
import re
url='https://www.zhanqi.tv/games'
header={'Referer':'https://www.zhanqi.tv/','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
r=geturl(url,headers=header)
id=re.findall(r'a href="(.+?)"',r)
claName=re.findall(r'class="name">(.+?)<',r)
for i in range(0,42):
    del id[0]
#print(id)
d=dict(zip(claName,id))
xs=list(d.keys())
for x,y in d.items():
    print(x,y)
    del d[xs[0]]
    if xs.index(x)==0:
        break
print(d)
