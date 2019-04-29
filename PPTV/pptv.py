import re
from DPL频道列表模板 import lists
import  string
import time
import os
from requestget import geturl
ns={'黑龙江卫视':'300172','河北卫视':'300143','甘肃卫视':'300148','河南卫视':'300159','天津卫视':'300160','山东卫视':'300161','安徽卫视':'300162','江苏卫视':'300163','中国教育-1':'300165','贵州卫视':'300174','山西卫视':'300167','陕西卫视':'300170','吉林卫视':'300176',"四川卫视":'300177','广西卫视':'300178',"青海卫视":'300180',"宁夏卫视":'300187',}
name=ns.keys()
for x in name:
    headers={'User-Agent':'AppleCoreMedia/1.0.0.9A405 (iPad; U; CPU OS 5_0_1 like Mac OS X; zh_cn)','Referer':'http://m.pptv.com/'}
    #print(ns[x])
    url='http://web-play.pptv.com/webplay3-0-'+ns[x]+'.xml?version=6&type=mhpptv'
    #print(url)
    r=geturl(url,headers=headers)
    '''if ns[x]=='300173':

        ts='''
    #print(r)
    n1=r.find('ft="1" rid="')+len('ft="1" rid="')
    n2=r.find('">',n1)
    rid=r[n1:n2]
    #print(rid)
    x1=r.find('UTC">')+len('UTC">')
    x2=r.find('</key>',x1)
    k=r[x1:x2]
    n=time.time()
    t=int(n)
    ts='http://wangsu2.live.pptv.com/live/'+rid+"/"+str(t)+'.ts?type=mhpptv&k='+k
    print(x,ts)
print(url)
    #os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe',ts)


