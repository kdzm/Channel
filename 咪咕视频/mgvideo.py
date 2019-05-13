from MD5 import get_token
import string
from requestget import geturl
#http://live.miguvideo.com/live/v2/tv-data/70002091
#http://live.miguvideo.com/live/v2/tv-data/
#http://47.95.69.248/gslb/live?stream_id=cctv3&region=310000&isp=telecom&uuid=1w9e8ex5-uo4j-k1h6-e5d2-olkclokyegoh&ver=1.0.8
import time
from 咪咕视频.mgchaclass import mgreurl

'''
t=int(time.time())
clientId=get_token(message=str(t)).upper()
print(clientId)
url='http://yk.miguvideo.com/playurl/v1/play/playurlh5?contId='+651632657+'&rateType=2&clientId='+clientId
headers={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12F70 MicroMessenger/6.2.3 NetType/WIFI Language/zh_CN'}
r=geturl(url,headers=headers)
print(r)
n1=r.find('"url":"')+len('"url":"')
n2=r.find('"',n1)
playurl=r[n1:n2]
print(playurl)'''
a=mgreurl()
for x,y in a.items():
    print(x,y)
