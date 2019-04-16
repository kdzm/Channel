import string
import re
import os
file=open("E:IPTV.txt","r+",encoding='utf-8')
#encoding='utf-8'
#files=file.text
print(type(file))
f=file.read()
#lines=file.readlines()
p1=r'ChannelName.+?.smil'
pattern1=re.compile(p1)
channel=pattern1.findall(f)
p2 = r'",UserChannelID="[0-9]{2,4}",ChannelURL="'
pattern2 = re.compile(p2)
for x in channel:
    #p2=r'",UserChannelID=[0-9]{4}"",ChannelURL="'
    #pattern2 = re.compile(p2)
    #x=x.replace('ChannelName="',"")
    #x=re.sub(pattern2," ",x)
    #x = x.replace(',UserChannelID', "")
    #x = x.replace('",ChannelURL="', ":")
    #x = x.replace('"="', "=")
    print(x)
    #with open('广东电信IPTV.txt', 'a', encoding="utf-8") as f: f.write(x + "\n")
    #with open('广东电信IPTV2.txt', 'a', encoding="utf-8") as f: f.write(x + "\n")
file.close()