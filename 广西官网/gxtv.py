import string
from requestget import geturl
import time
chlist={'广西卫视':'1',"广西综艺":'2',"广西都市":'3',"广西新闻":'4'," 广西公共":'5',"广西影视":'6',"广西国际":'7',"精彩广西":'10'}
#chlist={'广西卫视':'1','广西综艺':'2','广西都市':'3','广西新闻':'4'}
for x in chlist.keys():
    #url='http://tv.gxtv.cn/Tv-'+chlist[x]+'.html'
    url='http://tv.gxtv.cn/TV-'+chlist[x]+'.html'
    headers={'Referer':url,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.0 Safari/537.36 Edg/75.0.14'}
    r=geturl(url,headers=headers)
    #if x=='广西综艺':
    #print(r)
    n1=r.find("cid': '")+len("cid': '")
    n2=r.find("'",n1)
    n3=r.find("token': '")+len("token': '")
    n4=r.find("'",n3)
    cid=r[n1:n2]
    token=r[n3:n4]
    #print(cid,token)
    t0=time.perf_counter()
    rurl='http://tv.gxtv.cn/player/?cid='+cid+'&token='+token
    t0 = time.perf_counter()
    #print(rurl)
    r2=geturl(rurl,headers=headers)
    #print(r2)
    x1=r2.find('Video_Fluent = "')+len('Video_Fluent = "')
    x2=r2.find('"',x1)
    Video_Fluent=r2[x1:x2]
    y1=r2.find('WsSecret = "')+len('WsSecret = "')
    y2=r2.find('"',y1)
    WsSecret=r2[y1:y2]
    z1=r2.find('WsTime = "')+len('WsTime = "')
    z2=r2.find('"',z1)
    WsTime=r2[z1:z2]
    #t0=time.perf_counter()
    playurl='http://zb.gxtv.cn/live/nn_live'+Video_Fluent+'.flv?wsSecret='+WsSecret+'&wsTime='+WsTime+'&temp_time='+str(t0)
    print(x,playurl)
t=time.time()
tx=t*1000
print(int(tx))