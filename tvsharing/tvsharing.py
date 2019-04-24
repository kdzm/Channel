import string
import re
import os
from DPL频道列表模板 import lists
file=open("C:\\Users\\Administrator\\Desktop\\node\\tvsharing.txt","r+",encoding='utf-8')
f=file.read()
#f=f.replace("\n","")
p1=r'.+?,'
pattern1=re.compile(p1)
name=pattern1.findall(f)
p2=r'http.+?[0-9]{10}'
pattern2=re.compile(p2)
url=pattern2.findall(f)
names=[]
with open('tvsharing.dpl', 'w', encoding="utf-8") as f: f.write('')
for x in range(len(name)):
    y=name[x].replace(",","")
    names.append(y)
#print(len(names))
#print(len(url))
with open('tvsharing.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in url:
    j=url.index(u)
    (x,y)=lists(names[j],u)
    with open('tvsharing.dpl', 'a+', encoding="utf-8") as f: f.write(str(j+1)+x + "\n"+str(j+1)+y+"\n"+str(j+1)+'*played*0\n')
file.close()
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\tvsharing\\tvsharing.dpl')