import os
import re
import sys
from DPL频道列表模板 import lists
file=open("C:\\Users\\Administrator\\PycharmProjects\\频道破解\\爱奇艺\\iqiyi.txt","r+",encoding='utf-8')
f=file.read()
name=re.findall(r'(.+?),',f)
url=re.findall(r'http.+?m3u8',f)
with open('iqiyi2.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('iqiyi2.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in url:
    j=url.index(u)
    (x,y)=lists(name[j],u)
    with open('iqiyi2.dpl', 'a+', encoding="utf-8") as f: f.write(str(j+1)+x + "\n"+str(j+1)+y+"\n"+str(j+1)+'*played*0\n')
file.close()
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\爱奇艺\\iqiyi2.dpl')
s=u'\u6cb3\u5357\u65b0\u519c\u6751\u9891\u9053'
#a=s.decode('raw_unicode_escape')
print(s)