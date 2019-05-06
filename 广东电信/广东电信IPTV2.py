import string
import re
import os
import pandas as pd
from converttohtml import convertoHtml

file=open("E:广东电信IPTV2.txt","r+",encoding='utf-8')
#encoding='utf-8'
#files=file.text
print(type(file))
f=file.read()
#lines=file.readlines()
p1=r'ChannelName.+?",'
pattern1=re.compile(p1)
channelname=pattern1.findall(f)
#print(channelname.index("收视指南"))
#channelname=channelname.replace("ChannelName="","").replace("'","")
p2 = r',ChannelURL="rtsp://.+?.smil'
pattern2 = re.compile(p2)
channellist=pattern2.findall(f)
file.close()
for x in range(len(channelname)):
    channelname[x] = channelname[x].replace('ChannelName="', "").replace('",', "")
    #p2=r'",UserChannelID=[0-9]{4}"",ChannelURL="'
    #pattern2 = re.compile(p2)
    #x=x.replace('ChannelName="',"")
    #x=re.sub(pattern2," ",x)
    #x = x.replace(',UserChannelID', "")
    #x = x.replace('",ChannelURL="', ":")
    #x = x.replace('"="', "=")
    #print(x)
print(channelname)
    #channelnamenew=[]
    #channelnamenew.append(x)
    #print(channelnamenew)
#y=channelname.index(x)
for  i in channelname:
    y = channelname.index(i)
    channellist[y]=channellist[y].replace(',ChannelURL="','')

    #print(i)
    #print(channellist[y])
    #with open('广东电信IPTV.txt', 'a', encoding="utf-8") as f: f.write(x + "\n")
    print(i,channellist[y])
    #with open('广东电信IPTV.html', 'a', encoding="utf-8") as f: f.write(i+channellist[y]+ "\n")

'''def convertoHtml(result,title):
    d={}
    index=0
    for t in title:
        d[t]=result[index]
        index=index+1
    df=pd.DataFrame(d)
    df = df[title]
    pd.set_option('display.max_colwidth', 1500)
    h = df.to_html(index=False)
    #pd.set_option('max_colwidth', 200)
    #pd.set_option('display.max_rows', None)
    #pd.set_option('display.max_colwidth', 1500)
    return h
'''
result = [channelname,channellist]
title = [u'频道名称',u'链接']
x=convertoHtml(result,title)
#with open('广东电信IPTV.html','w', encoding="utf-8") as f: f.write(x)
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Google Chrome.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\广东电信IPTV.html')