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
    baseurl=baseurl+"sd.live.m3u8"
    #print(m,baseurl)
    millis = int(round(time.time() * 1000))
    playerVersion ="4.12.180327_RC"
    refererurl ="http://www.hljtv.com/live/"
    #print(baseurl)
    md5str="192e532733724cc07a871cbcd5f47977"+playerVersion+refererurl+str(millis)+baseurl+"192e532733724cc07a871cbcd5f47977"
    #print(md5str)
    hash=get_token(md5str)
    #print(millis)
    #print(hash)
    url2=drm+"?refererurl="+refererurl+"&url="+baseurl+"&hash="+hash+"&playerVersion="+playerVersion+"&time="+str(millis)
    #http://www.hljtv.com/m2o/player/drmx.php?refererurl=http%3A%2F%2Fwww.hljtv.com%2Flive%2F&url=http%3A%2F%2Fstream1.hljtv.com%2Fhljgg%2Fsd%2Flive.m3u8&hash=b268334db19fb2a7f5452cd740faefb7&playerVersion=4.12.180327_RC&time=1554365853382
    #print(url2)
    playurl=geturl(url2,headers)
    print(m,playurl)