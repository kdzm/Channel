import requests
import string
import re
import time
from MD5 import get_token
from requestget import geturl
import hashlib
hljtvid={"黑龙江导视":"2","黑龙江卫视":"3","黑龙江都市":"4","黑龙江公共":"5","黑龙江农垦":"6","黑龙江少儿":"7","黑龙江文体":"8","黑龙江新闻":"9","黑龙江影视":"10"}
headers={'Referer':'http://www.hljtv.com/live/',"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36','Referer':'http://www.hljtv.com/live/','Host':'www.hljtv.com'}
name=hljtvid.keys()
for m in name:
    url="http://www.hljtv.com/m2o/player/channel_xml.php?id="+hljtvid[m]+"&extend=&url=http://www.hljtv.com/live/&access/token=&first=1"
    #url = "http://www.hljtv.com/m2o/player/channel_xml.php?id=8&extend=&url=http://www.hljtv.com/live/&access/token=&first=1"
    x=geturl(url,headers)
    n1=x.find('drm="1">')+len('drm="1">')
    n2=x.find('php')+3
    drm = x[n1:n2]
    #print(drm)
    n3=x.find('" baseUrl="')+len('" baseUrl="')
    n4=x.find('"><item url')
    baseurl = x[n3:n4]
    baseurl=baseurl+"sd/live.m3u8"
    #print(m,baseurl)
    n=time.time()
    #print(n)
    millis = int(n * 1000)
    #print(millis)
    playerVersion ="4.12.180327_RC"
    refererurl ="http://www.hljtv.com/"
    #print(baseurl)
    md5str='862DF6728D919D06E3182D5129832559'+playerVersion+refererurl+str(millis)+baseurl+'862DF6728D919D06E3182D5129832559'
    #print(md5str))
    hs=get_token(md5str)
    #print(millis)
    #print(hs)
    url2=drm+"?refererurl="+refererurl+"&url="+baseurl+"&hash="+hs+"&playerVersion="+playerVersion+"&time="+str(millis)
    #url2="http://www.hljtv.com/m2o/player/drmx.php?refererurl=http%3A%2F%2Fwww.hljtv.com%2Flive%2F&url=http%3A%2F%2Fstream1.hljtv.com%2Fhljgg%2Fsd%2Flive.m3u8&hash="+hs+"&playerVersion=4.12.180327_RC&time="+str(millis)
    #data:text/html,http://stream2.hljtv.com/hljwy/sd/live.m3u8?_upt=708d2cd31555672036
    #http://www.hljtv.com/m2o/player/drmx.php?playerVersion=4%2E12%2E180327%5FRC&refererurl=http%3A%2F%2Fwww%2Ehljtv%2Ecom%2Flive%2Ffolder423%2F&time=1555664832061&hash=a9cf43cb8e8f6a3a06f8adfdef542f59&url=http%3A%2F%2Fstream2%2Ehljtv%2Ecom%2Fhljwy%2Fsd%2Flive%2Em3u8
    #http://stream2.hljtv.com/hljwy/sd/live.m3u8?_upt=2ca7f1351555671118
    #http://stream2.hljtv.com/hljwy/sd.live.m3u8?_upt=3f0579421555671803
    #print(url2)
    #print(url2)
    playurl=geturl(url2,headers)
    print(m,playurl)