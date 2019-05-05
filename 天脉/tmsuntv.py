#tmsuntv
import string
import re
import os
from DPL频道列表模板 import lists
import subprocess
file=open("C:\\Users\\Administrator\\Desktop\\node\\tmsuntv.txt","r+",encoding='utf-8')
f=file.read()
p1=r'.+?,'
pattern1=re.compile(p1)
name=pattern1.findall(f)
names=[]
for x in range(len(name)):
    y=name[x].replace(",","")
    names.append(y)
#print(names)
p2=r'http.+?\n'
pattern2=re.compile(p2)
url=pattern2.findall(f)
urls=[]
for i in url:
    z=i.replace('\n',"")
    urls.append(z)
#print(len(url))
#print(len(names))
#print(url)
#print(names)
with open('tmsuntv.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('tmsuntv.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in urls:
    j=urls.index(u)
    (x,y)=lists(names[j],u)
    with open('tmsuntv.dpl', 'a+', encoding="utf-8") as f: f.write(str(j+1)+x + "\n"+str(j+1)+y+"\n"+str(j+1)+'*played*0\n')
file.close()
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\天脉\\tmsuntv.dpl')