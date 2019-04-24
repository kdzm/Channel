#广东电信125
import string
import re
import os
from DPL频道列表模板 import lists
import subprocess
file=open("C:\\Users\\Administrator\\Desktop\\node\\广东电信125.txt","r+",encoding='utf-8')
f=file.read()
p1=r'.+?,'
pattern1=re.compile(p1)
name=pattern1.findall(f)
names=[]
for x in range(len(name)):
    y=name[x].replace(",","")
    names.append(y)
#print(names)
p2=r'rtsp.+?.smil'
pattern2=re.compile(p2)
url=pattern2.findall(f)
#print(len(url))
#print(len(names))
#print(url)
#print(names)
with open('广东电信125.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('广东电信125.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in url:
    j=url.index(u)
    (x,y)=lists(names[j],u)
    with open('广东电信125.dpl', 'a+', encoding="utf-8") as f: f.write(str(j+1)+x + "\n"+str(j+1)+y+"\n"+str(j+1)+'*played*0\n')
file.close()
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\广东电信\\广东电信125.dpl')