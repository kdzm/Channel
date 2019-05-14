from requestget import geturl
from requestget import posturl
import requests
from DPL频道列表模板 import lists
import re
import os
qq='https://egame.qq.com/gamelist'
headers={'referer':'https://egame.qq.com/gamelist/1','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
#class1={'一起看':'2000000110','主机游戏':'2000000140'}
class1={'一起看':'2000000110'}
a=[]
b=[]
playurl=[]
def QQliveClass():
    r=geturl(qq,headers=headers)
    #print(r)
    layoutid=re.findall(r'a href="/livelist\?layoutid=.+?"',r)
    titles=re.findall(r'target="_blank" title=".+?"',r)
    for x in layoutid:
        layoutid[layoutid.index(x)]=x.replace('a href="/livelist?layoutid=','').replace('"','')
    for y in titles:
        titles[titles.index(y)]=y.replace('target="_blank" title="','').replace('"','')
    d=dict(zip(titles,layoutid))
    for x,y in d.items():
        print(x,y)
    return d
    #print(r)
m=QQliveClass()
for i,j in m.items():
    print(i)
    urls='https://egame.qq.com/livelist?layoutid='+j
    r=geturl(urls,headers=headers)
    #print(r)
    p1=r'a href="/.+?"'
    p2=r'target="_blank" title=".+?"'
    pattern1=re.compile(p1)
    pattern2=re.compile(p2)
for i in class1.values():
    listurl='https://egame.qq.com/livelist?layoutid='+i
    r=geturl(listurl,headers=headers)
    #print(r)
    p1=r'a href="/.+?"'
    p2=r'target="_blank" title=".+?"'
    pattern1=re.compile(p1)
    pattern2=re.compile(p2)
    namers=pattern1.findall(r)
    #print(namers)
    del(namers[0])
    ids=pattern2.findall(r)
    #print(len(namers))
    #print(len(ids))
#print(namers)
for x in namers:
    x=x.replace('a href="/','').replace('"','')
    a.append(x)
for y in ids:
    y=y.replace('target="_blank" title="','').replace('"','')
    b.append(y)
d=dict(zip(a,b))

for x,y in d.items():
    #print(x,y)
    rurl='https://egame.qq.com/'+x
    ru=geturl(rurl,headers=headers)
    '''
    if x=='616289265':
        print(ru)
    '''
    n1=ru.find('playUrl":"')+len('playUrl":"')
    n2=ru.find('flv',n1)+3
    playurl.append(ru[n1:n2])
    #print(y,ru[n1:n2])
with open('一起看.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('一起看.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
for u in playurl:
    j=playurl.index(u)
    (x,y)=lists(b[j], u)
    with open('一起看.dpl', 'a+', encoding="utf-8") as f: f.write(str(j + 1) + x + "\n" + str(j + 1) + y + "\n" + str(j + 1) + '*played*0\n')
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\企鹅电竞\\一起看.dpl')