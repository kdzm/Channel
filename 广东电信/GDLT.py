import string
import re
import os
from DPL频道列表模板 import lists
import subprocess
file=open("C:\\Users\\Administrator\\Desktop\\node\\GDLT.txt","r+",encoding='utf-8')
f=file.read()
p1=r'.+?,'
pattern1=re.compile(p1)
name=pattern1.findall(f)
names=[]
for x in range(len(name)):
    y=name[x].replace(",","")
    names.append(y)
#print(names)
p2=r'http.+?.id=.m3u8'
pattern2=re.compile(p2)
url=pattern2.findall(f)
#print(len(url))
#print(len(names))
#print(url)
#print(names)
with open('GDLT.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('GDLT.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in url:
    j=url.index(u)
    (x,y)=lists(names[j],u)
    with open('GDLT.dpl', 'a+', encoding="utf-8") as f: f.write(str(j+1)+x + "\n"+str(j+1)+y+"\n"+str(j+1)+'*played*0\n')
file.close()
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\广东电信\\GDLT.dpl')
#http://hls51-o.kascend.com/chushou_live/635e368b56234584bc64ff8422f443c6.m3u8  翡翠台
#http://116.199.5.51:8114/index.m3u8?Fsv_chan_hls_se_idx=10&FvSeid=1&Fsv_ctype=LIVES&Fsv_otype=1&Provider_id=&Pcontent_id=.m3u8