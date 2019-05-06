import string
import re
import os
from DPL频道列表模板 import lists
for x in range(1,326):
    if   x<=9:
        url="http://httpdvb.slave.ttcatv.tv:13164/playurl?playtype=live&protocol=hls&accesstoken=R5CA2B7CAU3090C010K77540044IFB84556FPBM3220A5DV1044EZ33519WE22942B42A1&&playtoken=&programid=420000000"+str(x)+".m3u8"
    elif x<=99:
        url="http://httpdvb.slave.ttcatv.tv:13164/playurl?playtype=live&protocol=hls&accesstoken=R5CA2B7CAU3090C010K77540044IFB84556FPBM3220A5DV1044EZ33519WE22942B42A1&&playtoken=&programid=42000000"+str(x)+".m3u8"
    elif x<=325:
        url = "http://httpdvb.slave.ttcatv.tv:13164/playurl?playtype=live&protocol=hls&accesstoken=R5CA2B7CAU3090C010K77540044IFB84556FPBM3220A5DV1044EZ33519WE22942B42A1&&playtoken=&programid=4200000"+str(x)+".m3u8"
    #print(url)
    #with open('tty.txt', 'a+', encoding="utf-8") as f:
     #   f.write(url+"\n"+"\n")
file=open("C:\\Users\\Administrator\\PycharmProjects\\频道破解\\tty.txt","r+",encoding='utf-8')
f=file.read()
f=f.replace("\n","")
p1=r'http.+?m3u8'
pattern1=re.compile(p1)
url=pattern1.findall(f)
p2=r'm3u8.+?http'
pattern2=re.compile(p2)
name=pattern2.findall(f)
names=[]
for x in range(len(name)):
    y=name[x].replace("m3u8","").replace('http',"")
    names.append(y)
#print(len(names))
#print(len(url))
#with open('tty.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in url:
    j=url.index(u)
    (x,y)=lists(names[j],u)
    #with open('tty.dpl', 'a+', encoding="utf-8") as f: f.write(str(j+1)+x + "\n"+str(j+1)+y+"\n"+str(j+1)+'*played*0\n')
file.close()
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\tty.dpl')