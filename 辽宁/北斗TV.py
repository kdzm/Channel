import os
import string
from requestget import geturl
import requests
import re
from DPL频道列表模板 import lists
list='http://bdapp.lntv.cn:8242/api/lntv/living/tv'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3761.0 Safari/537.36 Edg/75.0.127.0','Referer': 'http://bdapp.lntv.cn/e/extend/lntv/gt.php','Host': 'bdapp.lntv.cn'}
r=geturl(list,headers=headers)
#print(r)
p1=r'http:.+?","'
pattern1=re.compile(p1)
http=pattern1.findall(r)
p2=r':"update","name":".+?"'
pattern2=re.compile(p2)
name=pattern2.findall(r)
p3=r'name_abbr":".+?"'
pattern3=re.compile(p3)
name_abbr=pattern3.findall(r)
list=[]
name2=[]
#print(name_abbr)
id=[]
with open('北斗TV.dpl', 'w', encoding="utf-8") as f: f.write('')
for i in name_abbr:
    i=i.replace('name_abbr":"','').replace('"','')
    id.append(i)
print(id)
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
with open('北斗TV.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0'+'\n')
for m in list2:
    #print(x,y)
    j=list2.index(m)
    (x,y)=lists(name2[j],m)
    with open('北斗TV.dpl', 'a+', encoding="utf-8") as f: f.write(str(j + 1) + x + "\n" + str(j + 1) + y + "\n" + str(j + 1) + '*played*0\n')
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\Channel\\辽宁\\北斗TV.dpl')