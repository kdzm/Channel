import os
import re
from DPL频道列表模板 import lists
file=open("C:\\Users\\Administrator\\PycharmProjects\\频道破解\\四川电信\\成都电信.txt","r+",encoding='utf-8')
f=file.read()
name=re.findall(r'(.+?),',f)
url=re.findall(r'http.+?m3u8',f)
with open('成都电信.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('成都电信.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in url:
    j=url.index(u)
    (x,y)=lists(name[j],u)
    with open('成都电信.dpl', 'a+', encoding="utf-8") as f: f.write(str(j+1)+x + "\n"+str(j+1)+y+"\n"+str(j+1)+'*played*0\n')
file.close()
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\四川电信\\成都电信.dpl')